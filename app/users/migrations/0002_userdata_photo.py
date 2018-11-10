# Generated by Django 2.1.3 on 2018-11-10 08:06

import app.utils.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='photo',
            field=app.utils.fields.ResizeImageField(blank=True, null=True, upload_to='user_photo'),
        ),
    ]