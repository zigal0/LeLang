"""
Contains all views that are used in app.
"""
import json

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.core.cache import cache

from lelang.models import Term, Language


def index_page(request: HttpRequest) -> HttpResponse:
    """Main page of app."""
    user = get_user_model()
    user_number = user.objects.count()
    lang_number = Language.objects.count()
    if user_number == 0:
        avg_term_number = 0.0
    else:
        avg_term_number = round(Term.objects.all().count() / user_number, 1)
    context = {
        'user_number': user_number,
        'lang_number': lang_number,
        'avg_term_number': avg_term_number,
    }

    return render(
        request=request,
        template_name='main/index.html',
        context=context,
    )


def profile_page(request: HttpRequest) -> HttpResponse:
    """User page of app."""
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'main/profile.html')


def learning_page(request: HttpRequest) -> HttpResponse:
    """Page for learning words."""
    if not request.user.is_authenticated:
        return redirect('home')

    terms_db = Term.objects.\
        filter(
            user_id=request.user.id,
            is_learned=False,
        ).\
        values_list('word', 'translation')
    terms = [{
        'word': word,
        'translation': translation,
        } for word, translation in terms_db]

    term_number = len(terms)

    context = {
        'terms': json.dumps(terms),
        'term_number': term_number,
    }

    return render(
        request=request,
        template_name='main/learning.html',
        context=context
    )


def term_add_page(request: HttpRequest) -> HttpResponse:
    """Page for adding new word."""
    if not request.user.is_authenticated:
        return redirect('home')

    languages_db = Language.objects.values_list('short_name')
    languages_short = [short_name for (short_name,) in languages_db]

    context = {
        'languages_short': languages_short
    }

    return render(
        request=request,
        template_name='main/term_add.html',
        context=context,
    )


def term_list_page(request: HttpRequest) -> HttpResponse:
    """Page for presenting all words."""
    if not request.user.is_authenticated:
        return redirect('home')

    languages = Language.objects.values_list('id', 'full_name')
    tables = []

    for language_from in languages:
        for language_to in languages:
            if language_to[0] == language_from[0]:
                continue

            terms = Term.objects.filter(
                user_id=request.user.id,
                language_from=language_from[0],
                language_to=language_to[0],
            )

            term_number = len(terms)

            if term_number == 0:
                continue

            table_terms = [
                {
                    'word': term.word,
                    'translation': term.translation,
                    'is_learned': term.is_learned,
                } for term in terms
            ]

            learned_terms = [term for term in terms if term.is_learned]
            learned_percent = len(learned_terms) / term_number

            table = {
                'meta': {
                    'language_from': language_from[1],
                    'language_to': language_to[1],
                    'term_number': term_number,
                    'learned_percent': learned_percent,
                },
                'terms': table_terms,
            }

            tables.append(table)

    return render(
        request=request,
        template_name='main/term_list.html',
        context={"tables": tables},
    )


# AUTHENTICATION
def login_page(request: HttpRequest) -> HttpResponse:
    """Page for login in."""
    if request.user.is_authenticated:
        return redirect('home')

    login_form = AuthenticationForm()

    return render(
        request=request,
        template_name='auth/login.html',
        context={'login_form': login_form},
    )


def signup_page(request: HttpRequest) -> HttpResponse:
    """Page for registration."""
    if request.user.is_authenticated:
        return redirect('home')

    form: UserCreationForm
    form = UserCreationForm()

    return render(
        request=request,
        template_name='auth/signup.html',
        context={'register_form': form},
    )


def logout_page(request: HttpRequest) -> HttpResponse:
    """Page for logout."""
    logout(request)
    messages.info(request, 'You have successfully logged out.')

    return redirect('home')


# API
def api_term_add(request: HttpRequest) -> HttpResponse:
    """Page for adding new word."""
    if not request.user.is_authenticated or request.method != 'POST':
        return redirect('home')

    cache.clear()

    languages_db = Language.objects.values_list('id', 'short_name')
    languages_dict = {name: lang_id for lang_id, name in languages_db}

    language_from = str(request.POST.get('language-from'))
    language_to = str(request.POST.get('language-to'))
    new_word = str(request.POST.get('word')).strip().lower()
    translation = str(request.POST.get('translation')).strip().lower()
    user_id = request.user.id

    if language_from == language_to:
        messages.error(request, 'Languages should be different.')
    elif len(new_word) == 0:
        messages.error(request, 'Word should contain at least 1 letter.')
    elif len(translation) == 0:
        messages.error(request, 'Translation should contain at least 1 letter.')
    else:
        Term.objects. \
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

        messages.success(request, 'New term added.')

        return redirect('term-list')

    return redirect('term-add')


def api_login(request: HttpRequest) -> HttpResponse:
    """Page for adding new word."""
    if request.user.is_authenticated or request.method != 'POST':
        return redirect('home')

    cache.clear()

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

    return redirect('login')


def api_signup(request: HttpRequest) -> HttpResponse:
    """Page for adding new word."""
    if request.user.is_authenticated or request.method != 'POST':
        return redirect('home')

    cache.clear()

    form: UserCreationForm
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()

        login(request, user)
        messages.success(request, 'SignUp successful.')

        return redirect('home')

    messages.error(
        request,
        'Unsuccessful registration. Invalid information.',
    )

    return redirect('signup')
