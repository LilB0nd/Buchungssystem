from django import forms
from django.contrib.auth.forms import UserCreationForm
from Buchungssystem.models import UserProfile
from django.core.exceptions import ValidationError

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(max_length=30, required=True, help_text='Ihre Schulmail')
    #classes = forms.CharField(choices=Classes.objects.all())

    class Meta:
        model = UserProfile
        fields = ('email',)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if "@schule.bremen.de" not in email:
            print('FEHLER')
            raise forms.ValidationError("Bitte eine gültige Schul-Mail angeben")

        else:
            return email
