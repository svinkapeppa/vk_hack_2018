from django.contrib import admin

from .models import Pet, FakePet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']


@admin.register(FakePet)
class FakePetAdmin(admin.ModelAdmin):
    list_display = ['id']
