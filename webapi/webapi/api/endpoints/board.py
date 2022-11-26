from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import BoardSerializer
from base.models import Board, Task, Todo
from django.db import models
from django.db.models import Q
from django.core.serializers import serialize as ss
import json

@api_view(["GET"])
def get_board_list(request):
    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_board_detail(request, pk):
    board = Board.objects.filter(pk=pk).first()
    if not board:
        return Response()
    serializer = BoardSerializer(board, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_board_create(request):
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def post_board_update(request, pk):
    boards = Board.objects.get(pk=pk)
    serializer = BoardSerializer(instance=boards, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_board_delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return Response("Board successfully deleted!")

@api_view(['POST'])
def post_board_add_task(request, pk):
    board = Board.objects.get(pk=pk)
    task_pk = request.data.get("task_pk", 0)
    task = Task.objects.filter(pk=task_pk).first()
    if task:
        board.tasks.add()
        board.save()
    serializer = BoardSerializer(board, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def post_all_boards(request):

    boards_list = json.loads(request.data.get("data_list", []))

    board_ids = [board["pk"] for board in boards_list]
    boards = Board.objects.filter(pk__in=board_ids)

    for board, json_board in zip(boards, boards_list):
        Task.objects.filter(board__pk=board.pk).update(board=None, position=0)
        task_pks = [task["pk"] for task in json_board["fields"]["tasks"]] if json_board["fields"]["tasks"] else []
        tasks = Task.objects.filter(pk__in=task_pks).order_by("pk")
        tasks_json = sorted(json_board["fields"]["tasks"], key=lambda x: x["pk"])
        
        for task, json_task in zip(tasks, tasks_json):
            if task.pk == int(json_task["pk"]):
                task.position = int(json_task["fields"]["position"])
                task.board = board
                task.save()

                Todo.objects.filter(task__pk=task.pk).update(task=None, position=0)
                todo_pks = [todo["pk"] for todo in json_task["fields"]["todos"]] if json_task["fields"]["todos"] else []
                todos = Todo.objects.filter(pk__in=todo_pks).order_by("pk")
                todos_json = sorted(json_task["fields"]["todos"], key=lambda x: x["pk"])

                for todo, json_todo in zip(todos, todos_json):
                    if todo.pk == int(json_todo["pk"]):
                        todo.position = int(json_todo["fields"]["position"])
                        todo.task = task
                        todo.save()

    return Response()

@api_view(['POST'])
def get_all_boards(request):
    boards = Board.objects.all().prefetch_related(models.Prefetch("tasks", Task.objects.prefetch_related(models.Prefetch("todos", to_attr="pre_todos")), to_attr="pre_tasks"))
    json_boards = json.loads(ss("json", boards))

    for board, json_board in zip(boards, json_boards):
        tasks = board.pre_tasks
        json_tasks = json.loads(ss("json", tasks))

        json_board["fields"]["tasks"] = sorted(json_tasks, key=lambda x: x["fields"]["position"])

        for task, json_task in zip(tasks, json_tasks):
            todos = task.pre_todos
            json_todos = json.loads(ss("json", todos))

            json_task["fields"]["todos"] = sorted(json_todos, key=lambda x: x["fields"]["position"])
    
    return Response(json_boards)
