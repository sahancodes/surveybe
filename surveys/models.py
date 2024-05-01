from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from accounts.models import Account

# Create your models here.
class Survey(models.Model):

    class SurveyTypes(models.TextChoices):
        PERSONAL_COMFORT = "PC", _("Personal Comfort")
        INDOOR_AIR_QUALITY = "AQ", _("Indoor Air Quality")
        INDOOR_ENVIRONMENTAL_QUALITY = "EQ", _("Indoor Environmental Quality")

    survey_id = models.AutoField(primary_key=True)
    survey_name = models.CharField(max_length=200)
    survey_intro = models.TextField(max_length=1000)
    survey_points = models.PositiveSmallIntegerField(default=25)
    survey_type = models.CharField(
        max_length=2,
        choices=SurveyTypes.choices,
        default=SurveyTypes.PERSONAL_COMFORT,
    )

    def __str__(self):
        return self.survey_name


class Question(models.Model):

    class QuestionTypes(models.TextChoices):
        MULTICHOICE = "MCQ", _("Multiple Choice Questions")
        OPENENDED = "OPN", _("Open Ended")
        SELECTONE = "SEL", _("Single Selection")
        MULTISELECT = "MSL", _("Multiple Selections")
        ONESLIDER = "SLD", _("Single Slide Bar")
        MULTISLIDER = "MSD", _("Multiple Slide Bars")

    question_id = models.AutoField(primary_key=True)
    survey_index = models.ForeignKey(Survey, on_delete=models.PROTECT, default=1)
    question_text = models.CharField(max_length=150)
    instruction = models. CharField(max_length=200)
    question_type = models.CharField(
        max_length=3,
        choices=QuestionTypes.choices,
        default=QuestionTypes.MULTICHOICE
    )

    def __str__(self):
        return self.question_text
    
class Answer(models.Model):

    # class Meta:
    #     db_table = "answers"

    answer_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.PROTECT)
    answers = models.JSONField(null=True, blank=True)        #Using JSON format we can send answers suitable to different question types in Question class
    next_question_id = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.answer_id) + "  " + str(self.question_id)
    


    
class CompletedSurvey(models.Model):
    response_id = models.AutoField(primary_key=True)
    survey_id = models.CharField(max_length=30, default=1)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE, default=1)
    question_n_answer = models.JSONField()

    def __str__(self):
        return str(self.response_id) + " - " + str(self.user_id) + " - " + str(self.survey_id)