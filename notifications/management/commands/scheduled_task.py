from django.core.management.base import BaseCommand
from crontab import CronTab
from datetime import datetime

class Command(BaseCommand):
    help = 'Scheduled task to print a message'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(f'Scheduled Task!'))