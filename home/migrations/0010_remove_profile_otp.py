# Generated by Django 5.1.3 on 2024-12-30 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_mobole_profile_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='otp',
        ),
    ]
