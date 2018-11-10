import rest_framework_filters

from app.map.models import PetPoint


class PetPointFilter(rest_framework_filters.FilterSet):
    class Meta:
        model = PetPoint
        fields = {
            'type': ['exact'],
        }
