# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    # music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # url(r'album/add/$', views.GoodsCreate.as_view(), name='goods_add'),

    # url(r'album/(?P<pk>[0-9]+)/$', views.GoodsUpdate.as_view(), name='goods_update'),

]