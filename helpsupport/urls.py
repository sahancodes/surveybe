from django.contrib import admin
from django.urls import path
from helpsupport import views

urlpatterns = [
    path('getfaqs/', views.getfaqs),
    path('sendticket/', views.sendticket),
]