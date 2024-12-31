# Generated by Django 5.1.3 on 2024-12-24 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_product_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mobile',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(upload_to='images/'),
        ),
    ]