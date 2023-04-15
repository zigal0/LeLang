"""
Contains all views that are used in app.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from lelang.models import Word


def index(request: HttpRequest) -> HttpResponse:
    """Main page of app."""
    return render(request, 'main/index.html')


def learning(request: HttpRequest) -> HttpResponse:
    """Page for learning words."""
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'main/learning.html')


def word_add(request: HttpRequest) -> HttpResponse:
    """Page for adding new word."""
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'main/word_add.html')


def word_list(request: HttpRequest) -> HttpResponse:
    """Page for presenting all words."""
    if not request.user.is_authenticated:
        return redirect('home')

    words = Word.objects.filter(user_id=request.user.id).values()
    return render(
        request,
        template_name='main/word_list.html',
        context={"words": words},
    )


# AUTHENTICATION
def login_page(request: HttpRequest) -> HttpResponse:
    """Page for login in."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')

                return redirect('home')

            messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')

    form = AuthenticationForm()

    return render(
        request=request,
        template_name='auth/login.html',
        context={'login_form': form},
    )


def register_page(request: HttpRequest) -> HttpResponse:
    """Page for registration."""
    if request.user.is_authenticated:
        return redirect('home')

    form: UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            messages.success(request, 'Registration successful.')

            return redirect('home')

        messages.error(
            request,
            'Unsuccessful registration. Invalid information.',
        )

    form = UserCreationForm()

    return render(
        request=request,
        template_name='auth/register.html',
        context={'register_form': form},
    )


def logout_page(request: HttpRequest) -> HttpResponse:
    """Page for logout."""
    logout(request)
    messages.info(request, 'You have successfully logged out.')

    return redirect('home')
