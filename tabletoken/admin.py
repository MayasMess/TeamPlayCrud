from django.contrib import admin
from tabletoken.models import TableToken


class TableTokenAdmin(admin.ModelAdmin):
    list_display = ['key_team', 'key_player']


admin.site.register(TableToken, TableTokenAdmin)
