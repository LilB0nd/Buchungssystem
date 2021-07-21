import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic

from Buchungssystem.forms import *
from Buchungssystem.models import *
from .tokens import account_activation_token


# Create your views here.


class Login(LoginView):
    template_name = 'registration/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect("/")
        return render(request, 'registration/login.html', {'error': True})


class Logout(generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login')


class SignUP(generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'registration/register.html'
    form_class = UserCreateForm

    def get(self, request, *args, **kwargs):
        form = UserCreateForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if "verification" in self.request.POST:
            email = self.request.POST['email']
            email = email.split('@')
            form = UserCreateForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = email[0]
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your blog account.'
                message = render_to_string('registration/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                return render(request, 'registration/email_sent.html', {'form': form})
            else:
                return render(request, 'registration/register.html', {'form': form})

    @staticmethod
    def activate(request, uidb64, token):
        try:  # TRY
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = UserProfile.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            # return redirect('home')
            return redirect('/login')
        else:
            return HttpResponse('Activation link is invalid!')

"""
class IntroductionCourse(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'introductionCourse.html'
    model = IntroductionCourse

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        groups = Group.objects.get(user=user)
        introduction_course = IntroductionCourse.objects.all()
        permission = None
        for group in groups:
            if group.name == "Schüler":
                permission = "readonly"


        context['permission'] = permission
        context['course_list'] = introduction_course
"""


class Appoinment(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'appointment.html'
    model = Appointment

    def get_context_data(self, **kwargs):
        form = CalenderForm()
        device = Equipment.objects.all()
        return {'form': form, 'device': device}

    def post(self, request, *args, **kwargs):
        user = self.request.user
        if user.letter_of_acceptance and user.introduction_course:
            start_date = self.request.POST['start_date']
            end_date = self.request.POST['end_date']
            equipment = self.request.POST['Equipment']
            datetime_start_date = datetime.datetime.strptime(start_date, '%d.%m.%Y %H:%M')
            datetime_end_date = datetime.datetime.strptime(end_date, '%d.%m.%Y %H:%M')
            form = CalenderForm(request.POST)
            if form.is_valid():
                new_Appointment = Appointment()
                new_Appointment.user = user
                new_Appointment.Equipment = Equipment.objects.get(id=equipment)
                new_Appointment.start_date = datetime_start_date
                new_Appointment.end_date = datetime_end_date
                new_Appointment.save()
            else:
                return render(request, 'appointment.html', {'form': form})
                # EndDatum vor dem Startdatum
            return HttpResponse(start_date)

        else:
            # return hat keine Berechtigung den Raum zu buchen
            return HttpResponse(user.username)


class EquipmentView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = "Geräte/geräte.html"
    context_object_name = 'equipment_list'
    model = Equipment

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        group = Group.objects.get(user=user)
        permission = None
        if group.name == "Schüler":
            permission = "readonly"

        equipment_list = Equipment.objects.all()
        context['all'] = equipment_list
        context["permission"] = permission
        return context


class DeviceView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = "Geräte/detail_view.html"
    context_object_name = 'Device'
    model = Equipment

    def get_context_data(self, *, object_list=None, **kwargs):
        form = DeviceForm()
        context = super().get_context_data(**kwargs)
        user = self.request.user
        group = Group.objects.get(user=user)

        if group.name == "Schüler":
            permission = "readonly"
        else:
            permission = None

        context['group'] = group
        context['form'] = form
        context["permission"] = permission
        return context

    def post(self, *args, **kwargs):
        if "save" in self.request.POST:
            print("test")
        if "upload" in self.request.POST:
            img = self.request.POST['img']
            device = Equipment.objects.get(id=kwargs['pk'])
            device.img = img
            device.save()
            print(device)
        return HttpResponseRedirect("")


class Userview(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = "User/Users.html"
    context_object_name = "users"
    model = UserProfile


class Usersview(LoginRequiredMixin, generic.TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'User/Lehreransicht.html'

    def get_context_data(self, **kwargs):
        user = UserProfile.objects.all()
        dic = {"User": user}
        return dic


class IndexView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'Home/Homepage.html'
