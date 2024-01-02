from django.db import models

# Create your models here.
class Leaderboard(models.Model):
    level = models.SmallIntegerField(primary_key=True)
    contribution_addition = models.SmallIntegerField()
    lower_limit = models.SmallIntegerField()
    upper_limit = models.SmallIntegerField()

    def __str__(self):
        return str(self.level) + ' ' + str(self.lower_limit) + ' ' + str(self.upper_limit) + ' ' + str(self.contribution_addition)