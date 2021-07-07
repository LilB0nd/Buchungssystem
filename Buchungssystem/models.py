from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# # Create your models here.


class Equipment(models.Model):
    name = models.CharField()
    description = models.CharField()
    brand = models.CharField()
    purchase_date = models.DateField()
    qualification = models.CharField()
    room = models.CharField()

    def __str__(self):
        return str(self.name + '_' + str(self.id))

    class Meta:
        verbose_name = 'Gerät'
        verbose_name_plural = 'Geräte'



class UserProfile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Klasse = models.CharField(max_length=5)
    Einverstaedniserklaerung = models.BooleanField(default=False)
    Kursbelegung = models.BooleanField(default=False)
    Kurs_Date = models.DateField()
    Lehrer = models.BooleanField(default=False)

class Appointment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    start_time = models.TimeField()
    end_time = models.TimeField()


class annulated_Appointment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    start_time = models.TimeField()
    end_time = models.TimeField()