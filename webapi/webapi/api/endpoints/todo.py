from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import TodoSerializer
from base.models import Todo

@api_view(["GET"])
def get_todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_todo_detail(request, pk):
    todo = Todo.objects.filter(pk=pk).first()
    if not todo:
        return Response()
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_todo_create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def post_todo_update(request, pk):
    todo = Todo.objects.get(pk=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return Response("Board successfully deleted!")