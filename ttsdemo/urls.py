from django.conf.urls import url, include
from django.conf.urls.static import static

from ttsdemo import settings

from core.views import index, tts

base_url = settings.BASE_URL


urlpatterns = [
    url(base_url + '/' if base_url else '', include('core.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
