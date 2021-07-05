from django.db import models

from django.core.exceptions import ValidationError
#TODO ENCRYPTED PASSWORD
class Accounts(models.Model):
    Email = models.EmailField(max_length=254)
    Username = models.CharField(max_length=30)
    # password = models.EncryptedCharField(max_lenght=100)
    Vorname = models.CharField(max_length=30)
    Nachname = models.CharField(max_length=50)
    Klasse = models.Choices[
        ("dqi17", "DQI17"
         "dqi18", "DQI18"
         "dqi19", "DQI19"
         "dqi20", "DQI20")
    ]
    Einverstaendniserklaerung = models.BooleanField(default=0)
    Kursbelegt = models.BooleanField(default=0)


    def clean(self):
        Email = self.cleaned_data("Email")
        if "@schule.bremen.de" not in Email:
            raise ValidationError("Bitte benutze deine von der Schule verfügung gestellte Email")
        return Email

