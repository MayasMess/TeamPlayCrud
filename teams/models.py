from django.db import models
from account.models import Account


class Team(models.Model):
    name = models.CharField(max_length=25, unique=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
