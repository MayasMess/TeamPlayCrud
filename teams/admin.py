from django.contrib import admin
from teams.models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Team, TeamAdmin)
