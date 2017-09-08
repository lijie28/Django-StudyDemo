
from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [


    url(r'^$', views.IndexView.as_view(), name='index'),
    # music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # music/<album_id>/favourite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    url(r'album/add/$', views.AlbumCreate.as_view(), name='album_add'),

    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]
