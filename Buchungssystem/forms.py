from django import forms
from django.contrib.auth.forms import UserCreationForm
from Buchungssystem.models import UserProfile, Appointment, Equipment
from bootstrap_datepicker_plus import DateTimePickerInput
import datetime
from django.db.models import Q


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


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('name', 'description', 'brand', 'model', 'purchase_date', 'qualification', 'room', 'img')


class CalenderForm(forms.ModelForm):
    start_date = DateTimePickerInput()
    end_date = DateTimePickerInput()

    class Meta:
        model = Appointment
        fields = ['Equipment', 'start_date', 'end_date']
        today = str(datetime.datetime.now())
        choice = Equipment.objects.all()

        widgets = {
            'start_date': DateTimePickerInput(options={"format": 'DD.MM.YYYY HH:mm',
                                                       'sideBySide': True,
                                                       'calendarWeeks': True,
                                                       'minDate': today,
                                                       'daysOfWeekDisabled': [0, 6],
                                                       'stepping': 15,
                                                       'disabledHours': [0, 1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 21, 22,
                                                                         23, 24],
                                                       'useCurrent': False
                                                       }, attrs={'required': True}),
            'end_date': DateTimePickerInput(options={"format": 'DD.MM.YYYY HH:mm',
                                                     'sideBySide': True,
                                                     'calendarWeeks': True,
                                                     'minDate': today,
                                                     'daysOfWeekDisabled': [0, 6],
                                                     'stepping': 15,
                                                     'useCurrent': False
                                                     }, attrs={'required': True}),
        }

    def clean(self):
        cleaned_data = super(CalenderForm, self).clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        equipment = cleaned_data.get('Equipment')
        if start_date >= end_date:
            raise forms.ValidationError('Ihre Startzeit ist nach Ihrer Endzeit')

        clashing_reservations = Appointment.objects.filter(Equipment=equipment).filter(
            Q(start_date__lte=start_date, end_date__gte=start_date) |
            Q(start_date__lt=end_date, end_date__gte=end_date)
        )
        if clashing_reservations.exists():
            raise forms.ValidationError('Those dates clash with another reservation.')

        return cleaned_data
