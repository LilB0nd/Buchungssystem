# Generated by Django 3.2.5 on 2021-07-07 09:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Buchungssystem', '0003_auto_20210707_1116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Buchung', 'verbose_name_plural': 'Buchungen'},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='purchase_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 7, 9, 36, 49, 242610, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='course_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]