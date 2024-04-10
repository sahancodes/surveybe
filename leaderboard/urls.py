from django.contrib import admin
from django.urls import path
from leaderboard import views

urlpatterns = [
    path('ranks/', views.getranks),
    path('leaderstats/', views.getleaders),
]