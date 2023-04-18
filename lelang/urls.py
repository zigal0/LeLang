"""
URL configuration for lelang project.
"""

from django.contrib import admin
from django.urls import path, include

from lelang import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('learning/', views.learning, name='learning'),
    path('word-add/', views.word_add, name='word-add'),
    path('word-list/', views.word_list, name='word-list'),
    path('profile/', views.profile, name='profile'),
    path('admin/', admin.site.urls, name='admin'),
    path('__debug__/', include('debug_toolbar.urls')),
]
