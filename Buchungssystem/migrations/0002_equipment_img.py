# Generated by Django 3.2.5 on 2021-07-20 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buchungssystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='device_img'),
        ),
    ]
