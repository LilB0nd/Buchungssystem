from django.db import models
from django.contrib.auth.models import User, Group, Permission, ContentType
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# # Create your models here.


class Equipment(models.Model):  # Die Relatation für die Geräte
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=300, null=True, blank=True)
    brand = models.CharField(max_length=30, null=True, blank=True)
    model = models.CharField(max_length=30, null=True, blank=True)
    purchase_date = models.DateField(default=timezone.now)
    qualification = models.TextField(max_length=300)
    room = models.CharField(max_length=5, null=True, blank=True)
    img = models.ImageField(default='missing_image.png', upload_to='device_img/', blank=True, null=True)

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
    email = models.EmailField('email address', unique=True, blank=False, default="maxmustermann@schule.bremen.de")
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Klasse")
    letter_of_acceptance = models.BooleanField(default=False, verbose_name="Einverständniserklärung")
    introduction_course = models.BooleanField(default=False, verbose_name="Kurs belegt")

    def save(self, *args, **kwargs):  # Es wird überprüft ob die Schulmail eine Lehrer- oder Schülermail ist
        super(UserProfile, self).save(*args, **kwargs)
        stremail = str(self.email)
        if stremail[1] == '.':  # Mail mit einem Punkt an zweiter Stelle sind Lehrer Mails
            teacher_group = Group.objects.get_or_create(name='Lehrer',)
            teacher_group[0].user_set.add(self)
        else:
            student_group = Group.objects.get_or_create(name='Schüler')
            student_group[0].user_set.add(self)

        super(UserProfile, self).save(*args, **kwargs)  # Nutzer wird gespeichert

""" # Einführungkurs 
class IntroductionCourse(models.Model):
    orginazer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Veranstalter")
    start_date = models.DateTimeField(verbose_name="Startzeit", blank=True, null=True)
    end_date = models.DateTimeField(verbose_name="Endzeit", blank=True, null=True)
    user_list = models.ManyToManyField(UserProfile)
    places = models.IntegerField(blank=True, null=True)
"""


class Appointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Benutzer")
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="Gerät")
    start_date = models.DateTimeField(verbose_name="Start", blank=True, null=True)
    end_date = models.DateTimeField(verbose_name="Ende", blank=True, null=True)

    def __str__(self):
        return str('Buchung/' + str(self.start_date) + '-' + str(self.end_date))

    class Meta:
        verbose_name = 'Buchung'
        verbose_name_plural = 'Buchungen'

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)


class AnnulatedAppointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Benutzer")
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="Gerät")
    start_date = models.DateTimeField(verbose_name="Startzeit", blank=True, null=True)
    end_date = models.DateTimeField(verbose_name="Endzeit", blank=True, null=True)


class News(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Benutzer")
    content = models.CharField(max_length=500, blank=True, verbose_name="Inhalt")
    Date = models.DateField(blank=True, verbose_name="Datum")

