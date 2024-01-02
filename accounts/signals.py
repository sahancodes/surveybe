from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Account

@receiver(post_save, sender=User)
def create_account_handler(sender, instance, created, **kwargs):
    if not created:
        return
    #Create account only if its newly created
    print("Sender -->", sender)
    print("Instance -->", instance)
    print("Created? -->", created)
    account = Account(userid=instance)
    account.save()

    