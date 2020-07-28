from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from players.models import Player
from players.api.serializers import PlayerAllSerializer


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Player.objects.all()
    serializer_class = PlayerAllSerializer


class PlayerListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Player.objects.all()
    serializer_class = PlayerAllSerializer


class PlayerListByTeam(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlayerAllSerializer

    def get_queryset(self):
        team = self.kwargs['team_id']
        return Player.objects.filter(team=team)
