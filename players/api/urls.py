from django.urls import path
from players.api.views import PlayerDetail, PlayerListCreate, PlayerListByTeam, PlayerListByOwner


app_name = 'players'

urlpatterns = [
    path('', PlayerListCreate.as_view(), name='player-list-create'),
    path('<pk>', PlayerDetail.as_view(), name='player-details'),
    path('team/<team_id>', PlayerListByTeam.as_view(), name='player-list-by-team'),
    path('owner/<owner_id>', PlayerListByOwner.as_view(), name='player-list-by-owner')
]