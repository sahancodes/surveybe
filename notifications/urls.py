from django.contrib import admin
from django.urls import path
from notifications import views

urlpatterns = [
    path('addnotification/', views.addnotification),
    path('getnotifications/', views.getnotifications),
]