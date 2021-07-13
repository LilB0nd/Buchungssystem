
from django.contrib.auth.views import LoginView
from Buchungssystem.forms import UserCreateForm
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from Buchungssystem.models import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
# Create your views here.

class Calendar(generic.CreateView):
    template_name = "Kalendar/CalendarLen.html"


class Login(LoginView):
    template_name = 'registration/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect("/admin/")
        return render(request, 'registration/login.html', {'error': True})


class SignUP(generic.CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreateForm

    def get(self, request, *args, **kwargs):
        form = UserCreateForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if "verification" in self.request.POST:
            email = self.request.POST['email']
            print(email.split('@'))
            form = UserCreateForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                print(dir(user))
                print()
                print()
                print(vars(user))
                user.is_active = False
                #user.save()
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
                return HttpResponse('Please confirm your email address to complete the registration')
            else:
                form = UserCreateForm()
            return render(request, 'registration/register.html', {'form': form})

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
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')


class Calender1(generic.ListView):
    pass


class EquipmentView(generic.ListView):

    template_name = "Geräte/geräte.html"
    context_object_name = 'equipment_list'
    model = Equipment


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        equipment_list = Equipment.objects.all()
        context['all'] = equipment_list
        return context


class DeviceView(generic.DetailView):

    template_name = "Geräte/detail_view.html"
    context_object_name = 'Device'
    model = Equipment

class Userview(generic.TemplateView):
    template_name = 'Lehreransicht.html'
    def get_context_data(self, **kwargs):
        user = UserProfile.objects.all()
        dic = {
            "User" : user
        }
        return dic