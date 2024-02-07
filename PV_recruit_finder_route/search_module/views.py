from django.contrib.auth import authenticate, login
from django.contrib.sites import requests
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from .models import *

app_name = "search_module"

def index(request):
    context = {
        "num_guilds": Guild.objects.count(),
        "num_teams": Team.objects.count(),
        "num_recruits": Recruit.objects.count(),
    }
    return render(request, template_name="search_module/index.html",
                  context=context)


def recruits(request):
    context = {
        "num_recruits": Recruit.objects.count(),
        "all_recruits": Recruit.objects.all(),
    }
    return render(request, template_name="search_module/recruits.html",
                  context=context)


def teams(request):
    context = {
        "num_teams": Team.objects.count(),
        "all_teams": Team.objects.all(),
    }
    return render(request, template_name="search_module/teams.html",
                  context=context)


def guilds(request):
    context = {
        "num_guilds": Guild.objects.count(),
        "all_guilds": Guild.objects.all(),
    }
    return render(request, template_name="search_module/guilds.html",
                  context=context)


auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=1204777768374771804&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Flogin%2F&scope=identify+guilds"
def home(request: HttpRequest) -> JsonResponse:
  return JsonResponse({ "msg": "Hello World" })

def get_authenticated_user(request: HttpRequest):
    print(request.user)
    user = request.user
    return JsonResponse({
        "id": user.id,
        "discord_tag": user.discord_tag,
        "avatar": user.avatar,
        "public_flags": user.public_flags,
        "flags": user.flags,
        "locale": user.locale,
        "mfa_enabled": user.mfa_enabled
    })


def discord_login(request: HttpRequest):
    return redirect(auth_url_discord)


def discord_login_redirect(request: HttpRequest):
    code = request.GET.get('code')
    print(code)
    user = exchange_code(code)
    discord_user = authenticate(request, user=user)
    discord_user = list(discord_user).pop()
    print(discord_user)
    login(request, discord_user)
    return redirect("/auth/user")


def exchange_code(code: str):
    data = {
        "client_id": "",
        "client_secret": "",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/oauth2/login/redirect",
        "scope": "identify"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post("https://discord.com/api/oauth2/token", data=data,
                             headers=headers)
    print(response)
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get("https://discord.com/api/v6/users/@me", headers={
        'Authorization': 'Bearer %s' % access_token
    })
    print(response)
    user = response.json()
    print(user)
    return user
