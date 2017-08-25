# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
# from views import go

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    # music/<album_id>/
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # music/<album_id>/
    url(r'^(?P<goods_id>[0-9]+)/$', views.goods_detail, name='detail'),

    url(r'add/$', views.add_goods, name='goods_add'),
    # url(r'goods/add/$', views.add_goods_get, name='goods_add_get'),

    # url(r'album/(?P<pk>[0-9]+)/$', views.GoodsUpdate.as_view(), name='goods_update'),

]