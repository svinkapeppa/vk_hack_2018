from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include

from app.map.views import map_urls
from app.pets.views import pets_urls
from app.users.views import user_urls

api_urls = [
    url(r'^users/', include(user_urls)),
    url(r'^map/', include(map_urls)),
    url(r'^pets/', include(pets_urls)),
]

urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
    url(r'^api/', include(api_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
