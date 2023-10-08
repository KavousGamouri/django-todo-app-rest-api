from rest_framework import serializers
from ...models import Task
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'author', 'task', 'description', 'completed', 'created_date']
        read_only_fields = ['author']

    def create(self, validated_data):
        validated_data['author'] = User.objects.get(id=self.context.get('request').user.id)
        return super().create(validated_data)
