from django.urls import path

from search_module.views import *

app_name = "search_module"

urlpatterns = [
    path("", index, name="index"),
    path("recruits/", recruits, name="recruits"),
    path("teams/", teams, name="teams"),
    path("guilds/", guilds, name="guilds"),
    path("login/", login_page, name="login"),
]
