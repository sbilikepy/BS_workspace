from django.shortcuts import render

from .models import *

app_name = "search_module"


# def index(request):  # 3
#     context = {
#         "num_drivers": Driver.objects.count(),
#         "num_manufacturers": Manufacturer.objects.count(),
#         "num_cars": Car.objects.count(),
#     }
#
#     return render(request, template_name="base.html", context=context)
def index(request):
    context = {
        "num_guilds" : Guild.objects.count(),
        "num_teams": Team.objects.count(),
        "num_recruits": Recruit.objects.count(),
    }
    return render(request, template_name="base.html", context=context)