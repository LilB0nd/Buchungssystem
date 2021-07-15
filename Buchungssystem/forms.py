from django import forms
from django.contrib.auth.forms import UserCreationForm
from Buchungssystem.models import UserProfile, Appointment
from bootstrap_datepicker_plus import DateTimePickerInput


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


class CalenderForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': DateTimePickerInput(options={"format": 'DD.MM.YYYY HH:mm',
                                                       'sideBySide': True,
                                                       'calendarWeeks': True}),
            'end_date': DateTimePickerInput(options={"format": 'DD.MM.YYYY HH:mm',
                                                     'sideBySide': True,
                                                     'calendarWeeks': True}),
        }

