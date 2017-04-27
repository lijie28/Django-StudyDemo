from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Sprint, Task

User = get_user_model()


class SprintSerializer(seriallizers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Sprint
        fields = ('id', 'name', 'description', 'end', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('sprint-detail',
                kwargs={'pk': obj.pk}, request=request)
        }

class TaskSerializer(seriallizers.ModelSerializer):
    """docstring for TaskSerializer"""
    assigned = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, required=False, allow_null = true, queryset=user.objects.all())
    status_display = seriallizers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'sprint',
         'status','status_display', 'order',
          'assigned', 'started', 'due', 'completed', )

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('sprint-detail',
                kwargs={'pk': obj.pk}, request=request)
        }



class UserSerializer(seriallizers.ModelSerializer):
    """docstring for UserSerializer"""
    full_name = serializers.CharField(source='get_full_name')

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', )



