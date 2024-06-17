from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('allprofiles/', views.accounts_list),
    path('signup/', views.signup),
    path('getuser/', views.getuser),
    path('isreg/', views.isreg),
    path('login/', views.loginuser),
    path('logout/', views.logout),
    path('isuser/', views.isuser),
    path('forgotpassword/', views.forgotpassword, name='forgot-password'),
    path('resetpassword/<str:token>/', views.resetpassword, name='reset-password'),
    path('changepassword/<str:token>/', views.changepassword, name='change-password'),
    path('changeuserdetails/<str:token>/', views.changeuserdetails),
    path('checkuseremail/', views.signupavailablity),
    path('user-survey-details/', views.get_user_survey_details, name='user-survey-details'),
]