# Generated by Django 5.1.3 on 2025-01-05 14:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='product_images/'),
            preserve_default=False,
        ),
    ]
