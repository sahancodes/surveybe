from django.db import models
from accounts.models import Account
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Feedback(models.Model):

    class FeedbackCategory(models.TextChoices):
        SURVEY = "SVY", _("Survey"),
        APP = "APP", _("Application"),
        LANGUAGE = "LNG", _("Language"),
        RANK = "RNK", _("Rank"),
        ACCOUNT = "ACT", _("Account"),
        NOTIFICATIONS = "NOT", _("Notifications"),

    feedback_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE, default=1)
    topic = models.CharField(max_length=50)
    body = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        choices=FeedbackCategory.choices, 
        default=FeedbackCategory.APP, 
        max_length=3,    
    )