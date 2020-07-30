from django.db import models
from account.models import Account
from teams.models import Team


class Player(models.Model):
    name = models.CharField(max_length=25)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
