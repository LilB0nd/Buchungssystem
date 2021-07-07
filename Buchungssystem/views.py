
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from Buchungssystem.models import *
# Create your views here.

class Login(LoginView):
    template_name = 'registration/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect("/admin/")
        return
