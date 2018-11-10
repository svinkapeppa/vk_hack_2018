from django.db import models

from app.utils.fields import ResizeImageField


class UserData(models.Model):
    vk_id = models.TextField(blank=True, null=True)
    photo = ResizeImageField(width=1000, height=1000, blank=True, null=True, upload_to='user_photo')
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    coins = models.IntegerField(default=0)
    donated = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователей'
