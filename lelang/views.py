"""
Contains all views that are used in app.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from lelang.models import Word


def index(request: HttpRequest) -> HttpResponse:
    """Main page of app."""
    return render(request, 'index.html')


def learning(request: HttpRequest) -> HttpResponse:
    """Page for learning words."""
    return render(request, 'learning.html')


def login(request: HttpRequest) -> HttpResponse:
    """Page for login in."""
    return render(request, 'login.html')


def register(request: HttpRequest) -> HttpResponse:
    """Page for registration."""
    return render(request, 'register.html')


def word_add(request: HttpRequest) -> HttpResponse:
    """Page for adding new word."""
    return render(request, 'word_add.html')


def word_list(request: HttpRequest) -> HttpResponse:
    """Page for presenting all words."""
    words = Word.objects.all()
    return render(request, 'word_list.html', context={"words": words})
