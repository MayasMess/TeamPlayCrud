from django.urls import path
from teams.api.views import TeamDetail


app_name = 'teams'

urlpatterns = [
    path('<pk>', TeamDetail.as_view(), name='teams')
]
