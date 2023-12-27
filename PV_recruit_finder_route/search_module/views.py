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
    return render(request, template_name="base.html", context=context)


def recruits(request):
    context = {
    }
    now = datetime.now()
    data = [i.nickname for i in Recruit.objects.all()]
    html = f"<html><body>Formed at: [{now}] <br>Recruits list: {data}</body></html>"
    return HttpResponse(html)

def teams(request):
    context = {
    }
    now = datetime.now()
    data = [i.team_name for i in Team.objects.all()]
    html = f"<html><body>Formed at: [{now}] <br>Teams list: {data}</body></html>"
    return HttpResponse(html)


def guilds(request):
    context = {
    }
    now = datetime.now()
    data = [i.name for i in Guild.objects.all()]
    html = f"<html><body>Formed at: [{now}] <br>Recruits list: {data}</body></html>"
    return HttpResponse(html)


def login_page(request):
    context = {
    }
    now = datetime.now()
    html = f"<html><body>Login request formed at: [{now}] <br></body></html>"
    return HttpResponse(html)