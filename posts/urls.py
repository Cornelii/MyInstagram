from django.urls import path
from . import views

app_name="posts"


url_patterns = [
        path('create/', views.creat, name='create'),
    ]