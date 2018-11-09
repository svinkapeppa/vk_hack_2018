from django.db import models


class UserData(models.Model):
    vk_id = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    coins = models.IntegerField(default=0)
    donated = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователей'
