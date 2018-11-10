from rest_framework import serializers

from app.utils.geo_fields import PointField
from .models import PetPoint


class PetPointSerializer(serializers.ModelSerializer):
    location = PointField()

    class Meta:
        model = PetPoint
        fields = ('name', 'type', 'address', 'location', 'site', 'extra')
