import os

from django.conf.urls import url
from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .filters import PetFilter
from .forms import PhotoUploadForm
from .models import Pet, FakePet
from .serializers import PetSerializer
from .view_utils import calculate_embeddings_and_get_distances


def get_photos():
    paths = []

    for dirpath, _, filenames in os.walk('app/media/pets_photo'):
        for f in filenames:
            paths.append(os.path.abspath(os.path.join(dirpath, f)))

    return paths


class PetViewSet(mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 GenericViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_class = PetFilter


class FindSimilarView(APIView):
    def post(self, request):
        form = PhotoUploadForm(request.POST, request.FILES)
        if not form.is_valid():
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        m = FakePet.objects.create(**form.cleaned_data)
        data = calculate_embeddings_and_get_distances(m.photo.path, get_photos())
        return Response(data, status=status.HTTP_200_OK)

    def get(self, request):
        form = PhotoUploadForm()
        return render(request, 'find_similar.html', {'form': form})


router = DefaultRouter()
router.register(r'pets', PetViewSet)
urlpatterns = router.urls

pets_urls = [
    url(r'similar/', FindSimilarView.as_view())
] + urlpatterns
