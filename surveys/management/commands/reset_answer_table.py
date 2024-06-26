# app/management/commands/reset_table.py
from django.core.management.base import BaseCommand
from surveys.models import Answer

class Command(BaseCommand):
    help = 'Deletes all entries from a table and resets the primary key sequence.'

    def handle(self, *args, **kwargs):
        Answer.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All entries deleted from the table.'))

        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM surveys_answer;")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='surveys_answer';")  # For SQLite
        self.stdout.write(self.style.SUCCESS('Primary key sequence reset for the table.'))
