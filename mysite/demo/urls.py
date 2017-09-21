# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
# from views import go

app_name = 'demo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]