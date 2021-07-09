
from django.contrib.auth.views import LoginView
from Buchungssystem.forms import UserCreateForm
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from Buchungssystem.models import *
from verify_email.email_handler import send_verification_email
# Create your views here.


class Login(LoginView):
    template_name = "registration/login.html"

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

    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            print("TEST")
            inactive_user = send_verification_email(request, form)

    """ 
    template_name = 'registration/register.html'
    form_class = UserCreateForm

    def get(self, request, *args, **kwargs):
        context = {'form': UserCreateForm()}
        return render(request, 'registration/register.html', context)


"""
