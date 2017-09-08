# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
# from views import go

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<goods_id>[0-9]+)/$', views.goods_detail, name='detail'),
]