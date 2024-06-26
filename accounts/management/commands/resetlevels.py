from django.core.management.base import BaseCommand
from accounts.models import Account

class Command(BaseCommand):
    help = 'Reset all contribtion values of all users and reset levels'

    def handle(self, *args, **kwargs) :
        Account.objects.update(level=1, contribution = 0, rank = None)
        self.stdout.write(self.style.SUCCESS(f'Successfully reset all levels and contributions'))
