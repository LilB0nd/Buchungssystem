from django import forms
from Buchungssystem.models import UserProfile, Classes
from django.contrib.auth.forms import UserCreationForm



class UserCreateForm(UserCreationForm):
    email = forms.EmailField(max_length=30, required=True, help_text='Ihre Schulmail')
    username = forms.CharField(max_length=30, required=True)
    firstname = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=30, required=False)
    #classes = forms.CharField(choices=Classes.objects.all())

    class Meta:
        model = UserProfile
        fields = ('email', 'username', 'firstname', 'lastname')
