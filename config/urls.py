from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from app.users.views import user_urls
from app.map.views import map_urls

api_urls = [
    url(r'^users/', include(user_urls)),
    url(r'^map/', include(map_urls)),
]

urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
    url(r'^api/', include(api_urls)),
]
