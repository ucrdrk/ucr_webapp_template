from django.urls import path
from django.conf.urls import url
from account.api import views
from account.api.views import(
    registration_view,userGameAPI,UserSyncAPI,UserGameApiView
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = "account"

urlpatterns = [
    path('register', registration_view, name = 'register'),
    path('login', obtain_auth_token, name = 'login'),
    path('user_game', UserGameApiView.as_view(), name='user_game'),
    url(r'^userGame$',views.userGameAPI),
    url(r'^userGame/([0-9]+)$',views.userGameAPI),
    url(r'^UserSync$',views.UserSyncAPI),
    url(r'^UserSync/([0-9]+)$',views.UserSyncAPI)

    #url(r'^userGame/$', userGameAPI, name='userGame')
]
