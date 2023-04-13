"""
Contains all views that are used in app.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from lelang.models import User


def index(request: HttpRequest) -> HttpResponse:
    """
    Return main page of app.
    """
    users = User.objects.all()
    return render(request, "index.html", context={"users": users})
