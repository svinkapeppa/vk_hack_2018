from django.contrib import admin

from app.users.models import UserData


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['vk_id', 'first_name', 'last_name', 'level', 'experience', 'coins', 'donated']
