from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.views import generic

from .models import *


def index(request: HttpRequest) -> HttpResponse:
    context = {"num_books": Book.objects.count(),
               "num_authors": Author.objects.count(),
               "num_literary_formats": LiteraryFormat.objects.count(),
               "literary_format_list": LiteraryFormat.objects.all()
               }
    return render(
        request,
        "catalog/index.html",
        context=context)


# def literary_format_list_view(request: HttpRequest) -> HttpResponse:
#     literary_format_list = LiteraryFormat.objects.all()
#     context = {
#         "literary_format_list": literary_format_list
#     }
#     return render(
#         request,
#         "catalog/literary_format_list.html",
#         context=context)


class LiteraryFormatListView(generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"
    # queryset = LiteraryFormat.objects.filter(name__startswith="example")


class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.select_related("format")  # ORM N+1 issue fixed by select_related
    paginate_by = 10


def book_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        context = {
            "book": Book.objects.get(id=pk)
        }
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, template_name="catalog/book_detail.html", context=context)
