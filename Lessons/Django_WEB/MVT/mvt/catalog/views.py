from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import SomeModel, SomeModel_two

app_name = "catalog"
# TAXI analog


def index(request):
    print(SomeModel.objects.count())
    print(SomeModel.objects.all())
    print(type(SomeModel.objects.all()))
    #     return HttpResponse('<html>'
    #                         f"<h1>{SomeModel.objects.count()}</h1>"
    #                         f"<h2>{SomeModel_two.objects.count()}</h2>"
    #                         "<html>"
    # )
    context = {"num1": SomeModel.objects.count(), "num2": SomeModel_two.objects.count()}
    return render(request, template_name="index.html", context=context)


def hello_world(request: HttpRequest, unique_number: int = 0) -> HttpResponse:
    # http://127.0.0.1:8000/hello/?param1=asd
    print(request.GET)

    return HttpResponse(
        f"<html>"
        f"<h1>"
        f"text: Hello world {unique_number if unique_number != 0 else ''}"
        f"</h1>"
        f"<h2>request.method: {request.method}<h2>"
        f"<h3>params: {[i[1] for i in request.GET.items()]}<h3>"
        f"</html>"
    )
