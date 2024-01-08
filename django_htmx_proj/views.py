import time

# from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect

from Login.models import Clients


def default(request):
    return render(request, "index.html")


# def clicked(request):
#     time.sleep(2)
#     return HttpResponse(render_to_string("clicked.html", request=request))


def my_view(request):
    return render(request, "my_template.html")


def load_data(request):
    data = "<p>This data is loaded via HTMX without JSON!</p>"
    return HttpResponse(render_to_string(data, request=request))


@csrf_protect
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # user = authenticate(request, username=username, password=password)
        user = Clients.objects.get(username=username, password=password)

        if user is not None:
            # login(request, user)
            # You can render a template to a string and return it as a response.
            rendered_template = render_to_string(
                "logged.html", request=request, context={"user": user}
            )
            return HttpResponse(rendered_template, content_type="text/html")
        else:
            return HttpResponse(render_to_string("error.html", request=request))
    return HttpResponse(render_to_string("login.html", request=request))


def success(request):
    return HttpResponse(render_to_string("success.html", request=request))
