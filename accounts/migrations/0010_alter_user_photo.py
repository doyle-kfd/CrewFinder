# Generated by Django 4.2.16 on 2024-11-13 15:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_user_experience_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='photo'),
        ),
    ]
