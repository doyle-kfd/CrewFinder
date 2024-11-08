# Generated by Django 4.2.16 on 2024-11-08 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='boat_image',
            field=models.ImageField(blank=True, null=True, upload_to='boat_images/'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='captain',
            field=models.ForeignKey(limit_choices_to={'role': 'captain'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]