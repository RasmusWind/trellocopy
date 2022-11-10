from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import TeamSerializer
from base.models import Team, Worker

@api_view(["GET"])
def get_team_list(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_team_detail(request, pk):
    team = Team.objects.filter(pk=pk).first()
    if not team:
        return Response()
    serializer = TeamSerializer(team, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_team_create(request):
    serializer = TeamSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def post_team_update(request, pk):
    team = Team.objects.get(pk=pk)
    serializer = TeamSerializer(instance=team, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_team_delete(request, pk):
    team = Team.objects.get(pk=pk)
    team.delete()
    return Response("Board successfully deleted!")

@api_view(['POST'])
def post_team_add_worker(request, pk):
    team = Team.objects.get(pk=pk)
    worker_pk = request.data.get("worker_pk", 0)
    worker = Worker.objects.filter(pk=worker_pk)
    if worker:
        team.workers.add(worker)
        team.save()
    serializer = TeamSerializer(team, many=False)
    return Response(serializer.data)