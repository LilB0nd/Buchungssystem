# Generated by Django 3.2.5 on 2021-07-07 09:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Buchungssystem', '0002_auto_20210707_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annulatedappointment',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='purchase_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 7, 9, 16, 11, 601400, tzinfo=utc)),
        ),
    ]