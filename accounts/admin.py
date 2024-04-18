from django.contrib import admin
from .models import Account, SurveyGroup

# Register your models here.
admin.site.register(Account)
admin.site.register(SurveyGroup)