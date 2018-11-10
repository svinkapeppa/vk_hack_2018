# Generated by Django 2.1.3 on 2018-11-09 22:54

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField(choices=[(0, 'Стандартная точка'), (7, 'Кэш-бокс'), (16, 'Пункт сбора')], default=0)),
                ('address', models.TextField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('site', models.TextField(blank=True, null=True)),
                ('extra', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Данные о точке',
                'verbose_name_plural': 'Данные о точках',
            },
        ),
    ]