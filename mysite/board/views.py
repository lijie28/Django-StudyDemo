# from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets, authentication, permissions
from .models import Sprint, Task
from .serializers import SprintSerializer, TaskSerializer, UserSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer


User = get_user_model()


class DefaultsMixin(object):
    """Default settings for view authentication, permissions"""
    authentication_class = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_class = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class SprintViewSet(viewsets.ModelViewSet):
    """api end poing for listing and creating sprints"""
    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer


class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """api end point for listing and creating tasks"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer


class Test(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    # request.POST
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    @api_view(['GET', 'POST'])
    def for_test(request):
        response = Response()
        response['data'] = 'test haha'
        if request.method == 'POST':
            return response

# class LoginViewSet(object):
#     """docstring for LoginViewSet"""
#     # request.POST
#     # @api_view(['GET', 'POST'])
#     def login_list(request):

#         # if request.method == 'GET':
#         #     lookup_field = User.USERNAME_FIELD.all()
#         #     serializer = UserSerializer(lookup_field, many=True)
#         # return Response(serializer.data)

#         if request.method == 'POST':
#             # serializer = UserSerializer(data=request.data)
#             # if serializer.is_valid():
#             #     serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
