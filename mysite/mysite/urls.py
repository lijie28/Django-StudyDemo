"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from board.urls import router

# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets


# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')


# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^music/', include('music.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^goodsmanage/', include('goods_manage.urls')),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

# urlpatterns = [
# ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
