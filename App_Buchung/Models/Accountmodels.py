from django.db import models
from django.core.exceptions import ValidationError
class Accounts(models.Model):
    Email = models.EmailField(max_length=254)
    Username = models.CharField(max_length=30)
    password = models.CharField(max_lenght=100)
    Vorname = models.CharField(max_length=30)
    Nachname = models.CharField(max_length=50)
    Klasse = models.Choices[
        ("dqi17", "DQI17"
         "dqi18", "DQI18"
         "dqi19", "DQI19"
         "dqi20", "DQI20")
    ]
    Einverstaendniserklaerung = models.BooleanField(default=0)
    Kursbelegung = models.BooleanField(default=0)
    def __str__(self):
        return self.Vorname
    def clean(self):
        if "@schule.bremen.de" not in self.Email:
            raise ValidationError("Bitte benutze deine von der Schule verfügung gestellte Email")
        return self.Email

