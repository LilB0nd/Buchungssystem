from django import forms
from django.contrib.auth.forms import UserCreationForm
from Buchungssystem.models import UserProfile, Appointment, Equipment
from bootstrap_datepicker_plus import DateTimePickerInput
import datetime


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
        today = str(datetime.datetime.now())
        choice = Equipment.objects.all()
        widgets = {
            'start_date': DateTimePickerInput(options={"format": 'DD.MM.YYYY HH:mm',
                                                       'sideBySide': True,
                                                       'calendarWeeks': True,
                                                       'minDate': today,
                                                       'daysOfWeekDisabled': [0, 6],
                                                       'stepping': 30,
                                                       'disabledHours': [0, 1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 21, 22,
                                                                         23, 24]
                                                       }, attrs={'required': True}),
            'end_date': DateTimePickerInput(options={"format": 'DD.MM.YYYY HH:mm',
                                                     'sideBySide': True,
                                                     'calendarWeeks': True,
                                                     'minDate': today,
                                                     'daysOfWeekDisabled': [0, 6]
                                                     }, attrs={'required': True}),
        }

