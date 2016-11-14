from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.videos, name='videos'),
    url(r'^(?P<torrent_id>[0-9]+)/$', views.detail, name='detail'),
]
