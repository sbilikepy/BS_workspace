from django.contrib import admin
from django.urls import path, include
from catalog.views import *

app_name = "catalog"

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("", index, name="index"),
    path(
        "literary-formats/",
        LiteraryFormatListView.as_view(),
        name="literary-formats-list",
    ),
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", book_detail_view(), name="book-detail"),
]
