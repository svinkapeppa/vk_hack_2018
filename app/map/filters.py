import rest_framework_filters

from .models import PetPoint


class PetPointFilter(rest_framework_filters.FilterSet):
    class Meta:
        model = PetPoint
        fields = {
            'type': ['exact'],
        }
