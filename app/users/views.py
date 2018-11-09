from django.conf.urls import url
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import UserData
from .serializers import UserDataSerializer, OrderingSerializer


class UserDataViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    """
    ViewSet для работы с пользователями ВК
    """
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


class LeaderboardViewSet(APIView):
    def get(self, request):
        serializer = OrderingSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ordering = serializer.validated_data.get('ordering', None)
        if ordering:
            ud = UserData.objects.all().order_by('-' + ordering)
        else:
            ud = UserData.objects.all()
        serializer = UserDataSerializer(ud, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


router = DefaultRouter()
router.register(r'users', UserDataViewSet)
urlpatterns = router.urls

user_urls = [
    url(r'leaderboard/', LeaderboardViewSet.as_view()),
] + urlpatterns
