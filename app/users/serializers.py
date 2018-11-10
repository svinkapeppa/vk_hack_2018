from rest_framework import serializers

import app.users.constants as c
from .models import UserData


class OrderingSerializer(serializers.Serializer):
    ordering = serializers.ChoiceField(c.ORDERING_CHOICES, required=False)


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ('vk_id', 'photo', 'first_name', 'last_name', 'level', 'experience', 'coins', 'donated')
