from rest_framework import serializers
from teams.models import Team


class TeamAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
