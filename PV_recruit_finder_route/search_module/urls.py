from django.urls import path
from search_module.views import index

app_name = "search_module"

urlpatterns = [
    path("", index, name="index"),
]
