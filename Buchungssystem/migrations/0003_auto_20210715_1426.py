# Generated by Django 3.2.5 on 2021-07-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buchungssystem', '0002_auto_20210715_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='start_time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ende'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start'),
        ),
    ]
