from django.urls import path
from . import views

urlpatterns = [
    path('sessions/oauth/google', views.google_oauth_handler, name='index'),
]
