# Generated by Django 4.2.16 on 2024-11-08 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0002_trip_boat_image_alter_trip_captain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='captain',
            field=models.ForeignKey(limit_choices_to={'role': 'Captain'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]