from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from ...models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        tasks = Task.objects.filter(author=self.request.user)
        return tasks
