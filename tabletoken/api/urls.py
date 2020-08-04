from django.urls import path
from tabletoken.api.views import TableTokenDetail


app_name = 'tabletoken'

urlpatterns = [
    path('<pk>', TableTokenDetail.as_view(), name='table-token'),
]