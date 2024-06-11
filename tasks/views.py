from rest_framework import viewsets, permissions
from .models import Task, Comment, TaskList
from .serializers import TaskSerializer, CommentSerializer, TaskListSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        # Allow superusers to perform all actions
        if self.request.user.is_superuser:
            return [permissions.IsAuthenticated()]

        # Normal users can only retrieve (view) tasks
        elif self.action in ['retrieve']:
            return [permissions.IsAuthenticated()]

        return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAuthenticated]
