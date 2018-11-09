from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include

api_urls = [
]

urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
    url('', include('social_django.urls')),
]
