from datetime import datetime

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import *

app_name = "search_module"


#
# path("recruits/", index, name="recruits"),
# path("teams/", index, name="teams"),
# path("guilds/", index, name="guilds"),
# path("login/", index, name="login"),
def index(request):
    context = {
        "num_guilds": Guild.objects.count(),
        "num_teams": Team.objects.count(),
        "num_recruits": Recruit.objects.count(),
    }
    return render(request, template_name="search_module/index.html", context=context)


def recruits(request):
    context = {
        "num_recruits": Recruit.objects.count(),
        "all_recruits": Recruit.objects.all(),
    }
    return render(request, template_name="search_module/recruits.html", context=context)


def teams(request):
    context = {
        "num_teams": Team.objects.count(),
        "all_teams": Team.objects.all(),
    }
    return render(request, template_name="search_module/teams.html", context=context)


def guilds(request):
    context = {
        "num_guilds": Guild.objects.count(),
        "all_guilds": Guild.objects.all(),
    }
    return render(request, template_name="search_module/guilds.html", context=context)


def login_page(request):
    context = {}
    now = datetime.now()
    html = f"<html><body>Login request formed at: [{now}] <br></body></html>"
    return HttpResponse(html)
