from django.db import models


class Equipment(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=99)
    description = models.CharField(max_lenght=300)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Gerät'
        verbose_name_plural = 'Geräte'
