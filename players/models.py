from django.db import models
from teams.models import Team


class Player(models.Model):
    name = models.CharField(max_length=25)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
