# Generated by Django 2.1.4 on 2019-01-08 10:09

import askcompany.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=askcompany.utils.uuid_upload_to),
        ),
    ]