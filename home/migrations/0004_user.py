# Generated by Django 5.1.3 on 2024-12-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_contact_usename'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('username', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('mobile', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=12)),
                ('confirmpassword', models.CharField(max_length=12)),
                ('date', models.DateField()),
            ],
        ),
    ]