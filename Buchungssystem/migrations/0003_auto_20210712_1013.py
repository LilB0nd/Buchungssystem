# Generated by Django 3.0.5 on 2021-07-12 08:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Buchungssystem', '0002_auto_20210712_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='course_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 7, 12, 8, 13, 26, 269754, tzinfo=utc), null=True, verbose_name='Kursbelegungsdatum'),
        ),
    ]
