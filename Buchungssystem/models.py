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
    purchase_date = models.DateField(default=timezone.now)
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
    course_date = models.DateField(blank=True, null=True, default=timezone.now)

    email = models.EmailField(('email address'), unique=True, blank=False, default="maxmustermann@schule.bremen.de")
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Klasse")
    letter_of_acceptance = models.BooleanField(default=False, verbose_name="Einverständniserklärung")
    induction_course = models.BooleanField(default=False, verbose_name="Kurs belegt")
    course_date = models.DateField(blank=True, null=True, default=timezone.now(), verbose_name="Kursbelegungsdatum")


class Appointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Benutzer")
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="Gerät")
    date = models.DateField(blank=True, verbose_name="Datum")
    start_time = models.TimeField(verbose_name="Start")
    end_time = models.TimeField(verbose_name="Ende")

    def __str__(self):
        return str('Buchung/' + str(self.date) + '/' + str(self.start_time) + '-' + str(self.end_time))

    class Meta:
        verbose_name = 'Buchung'
        verbose_name_plural = 'Buchungen'


class AnnulatedAppointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Benutzer")
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="Gerät")
    date = models.DateField(blank=True, verbose_name="Datum")
    start_time = models.TimeField(verbose_name="Start")
    end_time = models.TimeField(verbose_name="Ende")


class News(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Benutzer")
    content = models.CharField(max_length=500, blank=True, verbose_name="Inhalt")
    Date = models.DateField(blank=True, verbose_name="Datum")
