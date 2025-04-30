from django.urls import path
from . import views

urlpatterns = [
    path('', views.bug_list, name='bug_list'),
    path('new/', views.create_bug, name='create_bug'),
]