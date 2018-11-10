from django.contrib.gis.db import models

import app.map.constants as c


class PetPoint(models.Model):
    name = models.TextField(blank=True, null=True)
    type = models.IntegerField(choices=c.PET_POINT_TYPES, default=c.PET_POINT_DEFAULT)
    address = models.TextField(blank=True, null=True)
    location = models.PointField(srid=4326, null=True, blank=True)
    site = models.TextField(blank=True, null=True)
    extra = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Данные о точке'
        verbose_name_plural = 'Данные о точках'
