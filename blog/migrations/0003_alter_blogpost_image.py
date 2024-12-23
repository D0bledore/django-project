# Generated by Django 5.1.3 on 2024-12-17 10:43

import storages.backends.s3
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(storage=storages.backends.s3.S3Storage(), upload_to='media/'),
        ),
    ]
