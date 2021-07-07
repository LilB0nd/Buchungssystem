from django.db import models
# Create your models here.


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


class Appointment(models.Model):
    pass