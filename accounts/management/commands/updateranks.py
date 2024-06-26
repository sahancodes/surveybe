from django.core.management.base import BaseCommand
from django.db.models import F
from django.db import transaction
from accounts.models import Account  # Ensure you import your Account model correctly

def update_account_defaults_and_ranks():
    # Step 1: Update Null Levels and Contributions
    with transaction.atomic():
        accounts_to_update = Account.objects.filter(level__isnull=True, contribution__isnull=True)
        for account in accounts_to_update:
            account.level = 1 if account.level is None else account.level
            account.contribution = 5 if account.contribution is None else account.contribution
            account.save()

        # If you only want to fill null values without iterating through each object:
        Account.objects.filter(level__isnull=True).update(level=1)
        Account.objects.filter(contribution__isnull=True).update(contribution=5)
    
    # Step 2: Update Ranks
    # This should be done after the level and contribution updates to ensure ranks are calculated accurately.
    
    Account.update_ranks()


class Command(BaseCommand):
    help = 'Updates null level and contribution fields, and recalculates ranks for accounts'

    def handle(self, *args, **kwargs):
        update_account_defaults_and_ranks()
        self.stdout.write(self.style.SUCCESS('Successfully updated accounts'))