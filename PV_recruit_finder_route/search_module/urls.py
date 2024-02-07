from django.urls import path

from search_module.views import *

app_name = "search_module"

urlpatterns = [
    path("", index, name="index"),
    path("recruits/", recruits, name="recruits"),
    path("teams/", teams, name="teams"),
    path("guilds/", guilds, name="guilds"),
    path('auth/user/', get_authenticated_user,
         name='get_authenticated_user'),
    path('oauth2/', home, name='oauth2'),
    path('oauth2/login/', discord_login, name='oauth_login'),
    path('oauth2/login/redirect/', discord_login_redirect,
         name='discord_login_redirect')
]