from django.urls import path, include
from .views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'Task', TaskListViewSet, basename='task-list')
# router.register(r'Task-detail', TaskDetailViewSet, basename='task-detail')


urlpatterns = [
    # path('', include(router.urls)

    path('', TaskListViewSet.as_view({'get': 'list'  }), name='task_list'),
    path('<int:pk>/', TaskDetailViewSet.as_view({'get': 'retrieve', 'post': 'create', 'put': 'update',
                                                  'delete': 'destroy'}), name='task_detail'),
]