from django.contrib import admin
from django.contrib.gis.db import models
from mapwidgets import GooglePointFieldWidget

from app.map.models import PetPoint


@admin.register(PetPoint)
class PetPointAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'address', 'site']
    formfield_overrides = {
        models.PointField: {'widget': GooglePointFieldWidget},
    }
