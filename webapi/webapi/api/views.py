from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BoardSerializer, TaskSerializer, TodoSerializer, TeamSerializer, WorkerSerializer
from base.models import Board, Task, Todo, Team, Worker


