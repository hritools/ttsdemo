from django.conf.urls import url

from .views import index, tts


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^tts/$', tts, name='tts'),
]