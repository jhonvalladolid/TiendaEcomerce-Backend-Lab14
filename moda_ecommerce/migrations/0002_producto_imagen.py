# Generated by Django 5.0.6 on 2024-06-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moda_ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]