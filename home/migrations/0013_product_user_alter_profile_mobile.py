# Generated by Django 5.1.3 on 2024-12-31 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_profile_bio_profile_profile_pic_alter_profile_mobile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=12),
        ),
    ]