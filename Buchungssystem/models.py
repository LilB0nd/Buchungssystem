from django.contrib.auth import authenticate
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
# # Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=300)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    now = timezone.now()
    purchase_date = models.DateField(default=now)
    qualification = models.TextField(max_length=300)
    room = models.CharField(max_length=5)

    def __str__(self):
        return str(self.name + '/' + str(self.id))

    class Meta:
        verbose_name = 'Gerät'
        verbose_name_plural = 'Geräte'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    choices = [
        ("dqi18", "DQI18"),
        ("dqi19", "DQI19"),
        ("dqi20", "DQI20"),
        ("dqi21", "DQI21"),
    ]
    classes = models.CharField(max_length=5, choices=choices)
    letter_of_acceptance = models.BooleanField(default=False)
    induction_course = models.BooleanField(default=False)
    course_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.user.username)


class Appointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str('Buchung/' + str(self.date) + '/' + str(self.start_time) + '-' + str(self.end_time))

    class Meta:
        verbose_name= 'Buchung'
        verbose_name_plural= 'Buchungen'


class AnnulatedAppointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user