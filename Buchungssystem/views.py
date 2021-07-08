
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views import generic
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from Buchungssystem.models import *
# Create your views here.


#class Login(LoginView):
    #template_name = 'registration/login.html'

    #def get_context_data(self, **kwargs):
        #context = {'error_message': None}
        #return context

    #def post(self, request, *args, **kwargs):
        #username = request.POST['username']
        #password = request.POST['password']
        #user = authenticate(username=username, password=password)
        #if user is not None and user.is_active:
            #login(request, user)
            #return HttpResponseRedirect("/admin/")
        #messages.error(request, 'Fehlerhafte Anmeldedaten')
        #return HttpResponseRedirect(request.path)

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("/n1.html")# Redirect to a success page.
    return render(request, 'enter.html', {'login_form': form })

class SignUP(generic.CreateView):
    pass

