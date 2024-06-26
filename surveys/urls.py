from django.contrib import admin
from django.urls import path
from surveys import views

urlpatterns = [
    path('getsurvey/', views.getsurvey),
    path('savesurvey/', views.savesurvey),
    path('getsurveydetails/', views.getsurveydetails),
]