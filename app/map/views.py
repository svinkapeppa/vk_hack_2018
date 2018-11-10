from rest_framework import mixins
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import GenericViewSet

from .filters import PetPointFilter
from .models import PetPoint
from .serializers import PetPointSerializer


class MapViewSet(mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 GenericViewSet):
    """
    ViewSet для работы с пользователями ВК
    """
    queryset = PetPoint.objects.all()
    serializer_class = PetPointSerializer
    filter_class = PetPointFilter


router = DefaultRouter()
router.register(r'map', MapViewSet)
urlpatterns = router.urls

map_urls = [
] + urlpatterns
