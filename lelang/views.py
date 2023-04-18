"""
Contains all views that are used in app.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.core.cache import cache

from lelang.models import Word, Language


def index(request: HttpRequest) -> HttpResponse:
    """Main page of app."""
    user = get_user_model()
    user_number = user.objects.count()
    lang_number = Language.objects.count()
    if user_number == 0:
        avg_word_number = 0.0
    else:
        avg_word_number = round(Word.objects.all().count() / user_number, 1)
    context = {
        'user_number': user_number,
        'lang_number': lang_number,
        'avg_word_number': avg_word_number,
    }

    return render(
        request=request,
        template_name='main/index.html',
        context=context,
    )


def profile(request: HttpRequest) -> HttpResponse:
    """User page of app."""
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'main/profile.html')


def learning(request: HttpRequest) -> HttpResponse:
    """Page for learning words."""
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'main/learning.html')


def word_add(request: HttpRequest) -> HttpResponse:
    """Page for adding new word."""
    if not request.user.is_authenticated:
        return redirect('home')

    languages = Language.objects.values_list('id', 'short_name')
    language_short_names = [short_name for _, short_name in languages]

    languages_dict = {name: lang_id for lang_id, name in languages}
    context = {
        'languages': language_short_names
    }

    if request.method == 'POST':
        cache.clear()

        language_from = str(request.POST.get('language-from'))
        language_to = str(request.POST.get('language-to'))
        new_word = str(request.POST.get('word')).strip()
        translation = str(request.POST.get('translation')).strip()
        user_id = request.user.id

        if language_from == language_to:
            messages.error(request, 'Languages should be different.')
        elif len(new_word) == 0:
            messages.error(request, 'Word should contain at least 1 letter.')
        elif len(translation) == 0:
            messages.error(request, 'Translation should contain at least 1 letter.')
        else:
            Word.objects. \
                update_or_create(
                    word=new_word,
                    language_from_id=languages_dict[language_from],
                    language_to_id=languages_dict[language_to],
                    user_id=user_id,
                    defaults={
                        'translation': translation,
                        'is_learned': False,
                    }
                )

            messages.success(request, 'New word added.')

            return redirect('word-list')

    return render(
        request=request,
        template_name='main/word_add.html',
        context=context,
    )


def word_list(request: HttpRequest) -> HttpResponse:
    """Page for presenting all words."""
    if not request.user.is_authenticated:
        return redirect('home')

    words = Word.objects.filter(user_id=request.user.id)
    return render(
        request=request,
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
