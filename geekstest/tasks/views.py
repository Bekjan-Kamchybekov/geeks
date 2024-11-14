from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets


class TaskListViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class TaskDetailViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
