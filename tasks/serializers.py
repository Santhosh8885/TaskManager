from rest_framework import serializers
from .models import User, Task, Comment, TaskList

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'priority', 'due_date', 'completion_status', 'assigned_to']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'task', 'user', 'comment', 'created_at']

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ['id', 'name', 'is_public', 'owner', 'tasks']
