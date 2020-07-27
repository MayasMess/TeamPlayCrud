from django.shortcuts import render
from rest_framework import generics
from teams.models import Team
from teams.api.serializers import TeamDetailSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer
