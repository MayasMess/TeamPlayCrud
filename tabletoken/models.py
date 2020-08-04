from django.db import models


class TableToken(models.Model):
    key_team = models.CharField(max_length=40)
    key_player = models.CharField(max_length=40)
