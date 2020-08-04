import uuid

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from players.models import Player
from tabletoken.models import TableToken
from players.api.serializers import PlayerAllSerializer


def update_tabletoken_player_data():
    queryset = TableToken.objects.get(id=1)
    queryset.key_player = uuid.uuid4()
    queryset.save()


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Player.objects.all()
    serializer_class = PlayerAllSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        update_tabletoken_player_data()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        update_tabletoken_player_data()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlayerListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Player.objects.all()
    serializer_class = PlayerAllSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        update_tabletoken_player_data()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PlayerListByTeam(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlayerAllSerializer

    def get_queryset(self):
        team = self.kwargs['team_id']
        return Player.objects.filter(team=team)


class PlayerListByOwner(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlayerAllSerializer

    def get_queryset(self):
        owner = self.kwargs['owner_id']
        return Player.objects.filter(owner=owner)
