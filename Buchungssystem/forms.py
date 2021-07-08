from django import forms
from Buchungssystem.models import User, Classes


class UserCreateForm(forms.ModelForm):
    email = forms.EmailField(max_length=30, required=True, help_text='Ihre Schulmail')
    firstname = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=30, required=False)
    #classes = forms.CharField(choices=Classes.objects.all())

    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname')
