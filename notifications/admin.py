from django.contrib import admin
from .models import Notification, IssuedNotification

# # Register your models here.
admin.site.register(Notification)
admin.site.register(IssuedNotification)