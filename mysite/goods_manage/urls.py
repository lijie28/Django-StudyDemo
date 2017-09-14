from django.conf.urls import url
from . import views
# from views import go

app_name = 'goods_manage'

urlpatterns = [
    url(r'add/$', views.add_goods, name='add_goods'),
    url(r'add_attr/$', views.add_goods_attr, name='add_goods_attr'),
    url(r'success/$', views.add_success, name='add_success'),
    url(r'debug/$', views.debug, name='debug'),
]