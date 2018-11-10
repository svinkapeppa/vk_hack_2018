from rest_framework import mixins
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import GenericViewSet

from .filters import PetFilter
from .models import Pet
from .serializers import PetSerializer


class PetViewSet(mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 GenericViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_class = PetFilter


router = DefaultRouter()
router.register(r'pets', PetViewSet)
urlpatterns = router.urls

pets_urls = [
] + urlpatterns
