from django.db import models


class UserData(models.Model):
    vk_id = models.TextField(blank=True, null=True)
    experience = models.IntegerField(default=0)
    coins = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователей'
