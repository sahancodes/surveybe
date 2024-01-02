from django.db import models
from accounts.models import Account
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Ticket(models.Model):
    class TicketCategory(models.TextChoices):
        SURVEY = "SVY", _("Survey"),
        APP = "APP", _("Application"),
        LANGUAGE = "LNG", _("Language"),
        RANK = "RNK", _("Rank"),
        ACCOUNT = "ACT", _("Account"),
        NOTIFICATIONS = "NOT", _("Notifications"),

    ticket_id = models.AutoField(primary_key=True)
    user_id =models.ForeignKey(Account, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50)
    body = models.CharField(max_length= 500)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        choices=TicketCategory.choices, 
        default=TicketCategory.APP, 
        max_length=3
        )

    def __str__(self):
         return str(self.ticket_id) + " " + self.topic


class FAQ(models.Model):

    class FAQCategory(models.TextChoices):
        SURVEY = "SVY", _("Survey"),
        APP = "APP", _("Application"),
        LANGUAGE = "LNG", _("Language"),
        RANK = "RNK", _("Rank"),
        ACCOUNT = "ACT", _("Account"),
        NOTIFICATIONS = "NOT", _("Notifications"),

    faq_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=500)
    category = models.CharField(
        choices=FAQCategory.choices, 
        default=FAQCategory.APP, 
        max_length=3
        )

    def __str__(self):
         return str(self.faq_id) + " " + self.question