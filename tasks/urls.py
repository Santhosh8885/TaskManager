from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, CommentViewSet, TaskListViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'task-lists', TaskListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
