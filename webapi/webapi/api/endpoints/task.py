from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import TaskSerializer
from base.models import Task, Team

@api_view(["GET"])
def get_task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_task_detail(request, pk):
    task = Task.objects.filter(pk=pk).first()
    if not task:
        return Response()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def post_task_update(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return Response("Task successfully deleted!")

@api_view(['POST'])
def post_task_add_team(request, pk):
    task = Task.objects.get(pk=pk)
    team_pk = request.data.get("team_pk", 0)
    team = Team.objects.filter(pk=team_pk)
    if team:
        team.tasks.add(task)
        team.save()
    return Response()