from django.urls import path
from catalog.views import index
#TAXI analog

urlpatterns = [
    path('', index, name="index"),
    path('hello/', index),
]
