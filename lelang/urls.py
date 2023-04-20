"""
URL configuration for lelang project.
"""

from django.contrib import admin
from django.urls import path, include

from lelang import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),
    path('learning/', views.learning_page, name='learning'),
    path('term-add/', views.term_add_page, name='term-add'),
    path('term-list/', views.term_list_page, name='term-list'),
    path('profile/', views.profile_page, name='profile'),
    path('admin/', admin.site.urls, name='admin'),
    path('__debug__/', include('debug_toolbar.urls')),
]
