from django.conf.urls import url
from . import views
# from views import go

app_name = 'goods_manage'

urlpatterns = [
    url(r'add/$', views.add_goods, name='add_goods'),
    url(r'add/(?P<goods_id>[0-9]+)/$', views.add_goods_attr, name='add_goods_attr'),
]