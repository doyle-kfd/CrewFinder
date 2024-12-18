# Generated by Django 4.2.16 on 2024-11-14 06:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_rename_location_trip_departing_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='boat_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
