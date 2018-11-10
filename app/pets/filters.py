import rest_framework_filters

from .models import Pet


class PetFilter(rest_framework_filters.FilterSet):
    class Meta:
        model = Pet
        fields = {
            'type': ['exact'],
        }
