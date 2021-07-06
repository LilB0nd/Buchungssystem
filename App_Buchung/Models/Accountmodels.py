from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Profile(models.Model):
    Klasse = models.Choices[
        (
            "dqi18","DQI1818"
            "dqi19","DQI19"
            "dqi20","DQI20"
            "dqi21","DQI21")]
    Einverstaendniserklaerung = models.BooleanField(default=0)
    Kursbelegung = models.BooleanField(default=0)
    Kurs_date = models.DateTimeField()
    Lehrer = models.BooleanField(default=0)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
