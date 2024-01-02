from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import Account

# Create your models here.
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=50)
    text = models.TextField(max_length=300)

    def __str__(self):
        return str(self.notification_id) + " " + self.topic
    


class IssuedNotification(models.Model):

    class PriorityLevel(models.IntegerChoices):
        HIGH = 1, _("High"),
        MEDIUM = 2, _("Medium"),
        LOW = 3, _("Low"),

    issue_id = models.AutoField(primary_key=True)
    notification_id = models.CharField(max_length=50)
    priority = models.IntegerField(choices=PriorityLevel.choices,default=PriorityLevel.LOW)
    start_date = models.DateField(default='2023-12-08')
    end_date = models.DateField(default='2023-12-08')
    trigger_times = models.JSONField()
    user_id =models.ForeignKey(Account, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_id) + " " + str(self.notification_id) + " " + str(self.active)