from django.db import models

import app.pets.constants as c
from app.utils.fields import ResizeImageField


class Pet(models.Model):
    name = models.TextField(blank=True, null=True)
    type = models.IntegerField(choices=c.PET_TYPES, default=c.PET_DEFAULT)
    photo = ResizeImageField(width=1000, height=1000, blank=True, null=True, upload_to='pets_photo')

    class Meta:
        verbose_name = 'Обитатель приюта'
        verbose_name_plural = 'Обитатели приюта'
