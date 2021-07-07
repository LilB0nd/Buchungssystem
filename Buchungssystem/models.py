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
    course_date = models.DateField(blank=True)
    teacher = models.BooleanField(default=False)


class Appointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    start_time = models.TimeField()
    end_time = models.TimeField()


class AnnulatedAppointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    start_time = models.TimeField()
    end_time = models.TimeField()