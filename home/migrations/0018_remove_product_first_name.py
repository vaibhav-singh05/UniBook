# Generated by Django 5.1.3 on 2024-12-31 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_rename_name_product_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='first_name',
        ),
    ]
