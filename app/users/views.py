from rest_framework import mixins
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import GenericViewSet

from .models import UserData
from .serializers import UserDataSerializer


class UserDataViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    """
    ViewSet для работы с пользователями ВК
    """
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


router = DefaultRouter()
router.register(r'users', UserDataViewSet)
urlpatterns = router.urls

user_urls = [
] + urlpatterns
