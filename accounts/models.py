from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils.translation import gettext_lazy as _
from leaderboard.models import Leaderboard

# Create your models here.
class Account(models.Model):

    class Gender(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")

    class BestHours(models.TextChoices):
        MORNING = "M", _("Morning")
        EVENING = "E", _("Evening")

    class SelfStatement(models.TextChoices):
        STATEMENT1 = "Warm", _("I generally feel warmer than other people in the room")
        STATEMENT2 = "Same", _("In general, my experience is similar to others in terms of temperature")
        STATEMENT3 = "Cold", _("I generally feel colder than other people in the room")

    # username = models.OneToOneField(User, on_delete=models.CASCADE)
    
    userid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=0)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    userimg = models.ImageField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    gender = models.CharField(
        max_length= 1,
        choices=Gender.choices,
        default=Gender.MALE,
    )
    height = models.PositiveSmallIntegerField(null=True)
    weight = models.PositiveSmallIntegerField(null=True)
    best_hours = models.CharField(
        max_length=1,
        choices=BestHours.choices,
        default=BestHours.MORNING,
    )
    worksstarttime = models.TimeField(null=True)
    workendtime = models.TimeField(null=True)
    selfstatement = models.CharField(
        max_length=4,
        choices=SelfStatement.choices,
        default=SelfStatement.STATEMENT2,
    )
    rank = models.PositiveSmallIntegerField(null=True, blank=True)
    level = models.PositiveSmallIntegerField(null=True, blank=True)
    contribution = models.PositiveIntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    authtoken = models.CharField(max_length=255)
    

    def __str__(self):
        return  str(self.pk) + ' - ' + str(self.rank) + '-' + str(self.username) + ' - ' + str(self.email)

    @classmethod
    def update_ranks(cls):
        profiles = cls.objects.order_by('-contribution')
        for i, profile in enumerate(profiles, start=1):
            profile.rank = i
            profile.save()

    @classmethod
    def update_levels(cls, userid):
        profile = cls.objects.get(userid = userid)
        get_leaderboard_object = Leaderboard.objects.get(level = profile.level)
        if profile.contribution > get_leaderboard_object.upper_limit:
            profile.level = profile.level + 1
        profile.save()

    @classmethod
    def update_contribution(cls, userid):
        profile = cls.objects.get(userid = userid)
        get_leaderboard_object= Leaderboard.objects.get(level = profile.level)
        print(profile.level, get_leaderboard_object.level, get_leaderboard_object.contribution_addition)
        profile.contribution = profile.contribution + get_leaderboard_object.contribution_addition
        print(profile.contribution)
        profile.save()
 
class SurveyGroup(models.Model):
    from surveys.models import Survey
    group_id = models.AutoField(primary_key=True, auto_created=True)
    group_name = models.CharField(max_length=50)
    description = models.TextField()
    survey_id = models.ForeignKey(Survey, on_delete=models.CASCADE, default=1)
    members = models.ManyToManyField(Account, related_name="user_groups")
    start_date = models.DateField(default='2023-12-08')
    end_date = models.DateField(default='2023-12-08')
    trigger_times = models.JSONField(null=True)
    def __str__(self):
        return f"Group {self.group_id} {self.group_name}"
                
    