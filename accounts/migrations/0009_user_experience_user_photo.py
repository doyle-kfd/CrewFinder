# Generated by Django 4.2.16 on 2024-11-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='experience',
            field=models.CharField(choices=[('None', 'None'), ('RYA Competent Crew', 'RYA Competent Crew'), ('RYA Dayskipper', 'RYA Dayskipper'), ('RYA Yachtmaster Coastal', 'RYA Yachtmaster Coastal'), ('RYA Yachtmaster Offshore', 'RYA Yachtmaster Offshore'), ('RYA Yachtmaster Ocean', 'RYA Yachtmaster Ocean')], default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/'),
        ),
    ]
