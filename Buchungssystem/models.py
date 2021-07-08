from django.contrib.auth import authenticate
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
from django.contrib.auth.models import AbstractUser


# # Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=300, null=True, blank=True)
    brand = models.CharField(max_length=30, null=True, blank=True)
    model = models.CharField(max_length=30, null=True, blank=True)
    now = timezone.now()
    purchase_date = models.DateField(default=now)
    qualification = models.TextField(max_length=300)
    room = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return str(self.name + '/' + str(self.id))

    class Meta:
        verbose_name = 'Gerät'
        verbose_name_plural = 'Geräte'


class Classes(models.Model):
    name = models.CharField(max_length=12, default='keine Angabe')

    def __str__(self):
        return str('Klasse ' + self.name)

class UserProfile(AbstractUser):
    email = models.EmailField(('email address'),unique=True, blank=False,default="maxmustermann@schule.bremen.de")
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True, blank=True)
    letter_of_acceptance = models.BooleanField(default=False)
    induction_course = models.BooleanField(default=False)
    course_date = models.DateField(blank=True, null=True, default=timezone.now())




class Appointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str('Buchung/' + str(self.date) + '/' + str(self.start_time) + '-' + str(self.end_time))

    class Meta:
        verbose_name = 'Buchung'
        verbose_name_plural = 'Buchungen'


class AnnulatedAppointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
