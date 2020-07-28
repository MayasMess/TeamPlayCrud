from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from teams.models import Team
from teams.api.serializers import TeamAllSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Team.objects.all()
    serializer_class = TeamAllSerializer


class TeamListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Team.objects.all()
    serializer_class = TeamAllSerializer


class TeamListByOwner(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TeamAllSerializer

    def get_queryset(self):
        owner = self.kwargs['owner_id']
        return Team.objects.filter(owner=owner)
