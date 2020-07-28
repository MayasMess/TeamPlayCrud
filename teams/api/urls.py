from django.urls import path
from teams.api.views import TeamDetail, TeamListCreate, TeamListByOwner


app_name = 'teams'

urlpatterns = [
    path('', TeamListCreate.as_view(), name='team-list-create'),
    path('<pk>', TeamDetail.as_view(), name='team-details'),
    path('owner/<owner_id>', TeamListByOwner.as_view(), name='team-list-by-owner'),
]
