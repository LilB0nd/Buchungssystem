from django import forms
from django.contrib.auth.forms import UserCreationForm
from Buchungssystem.models import UserProfile
from django.core.exceptions import ValidationError

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(max_length=30, required=True, help_text='Ihre Schulmail')
    username = forms.CharField(max_length=30, required=True)
    #classes = forms.CharField(choices=Classes.objects.all())

    class Meta:
        model = UserProfile
        fields = ('email', 'username')

    def clean(self):
        if "@schule.bremen.de" not in self.email:
            print('FEHLER')
            raise ValidationError({"error_message": "Bitte eine gültige Schulemail angeben"})

        else:
            stremail = str(self.email)
            splittedmail = stremail.split('@')
            self.username = splittedmail[0]
