# Generated by Django 3.2.5 on 2021-07-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buchungssystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='img',
            field=models.ImageField(blank=True, default='missing_image.png', null=True, upload_to='media/device_img'),
        ),
    ]
