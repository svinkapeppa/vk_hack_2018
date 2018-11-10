from django.db import models

import app.pets.constants as c


class Pet(models.Model):
    name = models.TextField(blank=True, null=True)
    type = models.IntegerField(choices=c.PET_TYPES, default=c.PET_DEFAULT)

    class Meta:
        verbose_name = 'Обитатель приюта'
        verbose_name_plural = 'Обитатели приюта'
