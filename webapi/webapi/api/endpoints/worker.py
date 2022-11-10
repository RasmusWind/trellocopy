from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import WorkerSerializer
from base.models import Worker

@api_view(["GET"])
def get_worker_list(request):
    workers = Worker.objects.all()
    serializer = WorkerSerializer(workers, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_worker_detail(request, pk):
    worker = Worker.objects.filter(pk=pk).first()
    if not worker:
        return Response()
    serializer = WorkerSerializer(worker, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_worker_create(request):
    serializer = WorkerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def post_worker_update(request, pk):
    worker = Worker.objects.get(pk=pk)
    serializer = WorkerSerializer(instance=worker, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_worker_delete(request, pk):
    worker = Worker.objects.get(pk=pk)
    worker.delete()
    return Response("Board successfully deleted!")