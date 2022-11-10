from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import BoardSerializer
from base.models import Board, Task
from django.db import models
from django.db.models import Q

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
    boards_list = request.data.get("data_list", [])

    board_ids = [board["boardid"] for board in boards_list]
    boards = Board.objects.filter(pk__in=board_ids)

    for board, json_board in zip(boards, boards_list):
        Task.objects.filter(board__pk=board.pk).update(board=None, position=0)
        tasks = Task.objects.filter(pk__in=[task["taskid"] for task in json_board["tasks"]]).order_by("pk")
        tasks_json = sorted(json_board["tasks"], key=lambda x: x["taskid"])
        
        for task, json_task in zip(tasks, tasks_json):
            if task.pk == int(json_task["taskid"]):
                task.position = int(json_task["position"])
                task.board = board
                task.save()

    return Response()
