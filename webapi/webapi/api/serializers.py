from rest_framework import serializers
from base.models import Board, Task, Todo, Team, Worker

class BoardSerializer(serializers.Serializer):
    class Meta:
        model = Board
        fields = "__all__"

class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields = "__all__"

class TodoSerializer(serializers.Serializer):
    class Meta:
        model = Todo
        fields = "__all__"

class TeamSerializer(serializers.Serializer):
    class Meta:
        model = Team
        fields = "__all__"

class WorkerSerializer(serializers.Serializer):
    class Meta:
        model = Worker
        fields = "__all__"
