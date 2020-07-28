from django.urls import path
from account.api.views import registration_view, logout_view, ObtainAuthToken, get_user_by_token_view


app_name = 'account'

urlpatterns = [
    path('register', registration_view, name='register'),
    path('login', ObtainAuthToken.as_view(), name='login'),
    path('logout/<token>', logout_view, name='logout'),
    path('current-user/<token>', get_user_by_token_view, name='get-user')
]
