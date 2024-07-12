from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from accounts.models import Account
from django.utils import timezone

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
    unfolding_survey = models.BooleanField(default=False)
    survey_type = models.CharField(
        max_length=2,
        choices=SurveyTypes.choices,
        default=SurveyTypes.PERSONAL_COMFORT,
    )
    survey_time = models.PositiveSmallIntegerField(default=10)

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
    in_first_q_set = models.BooleanField(default=False)
    question_type = models.CharField(
        max_length=3,
        choices=QuestionTypes.choices,
        default=QuestionTypes.MULTICHOICE
    )

    def __str__(self):
        return str(self.question_id) + "  " + str(self.question_text)
    
class Answer(models.Model):

    # class Meta:
    #     db_table = "answers"

    answer_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.PROTECT)
    answers = models.JSONField(null=True, blank=True)        #Using JSON format we can send answers suitable to different question types in Question class
    # next_question_id = models.PositiveSmallIntegerField(null=True, blank=True)
    unfoldings = models.JSONField(null=True, blank=True)

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
    
    @classmethod
    def is_survey_submitted(cls, surveyid, userid):
        from accounts.models import SurveyGroup
        # Get the survey associated with this CompletedSurvey instance
        survey = Survey.objects.get(survey_id = surveyid)

        completed_surveys = cls.objects.filter(
            survey_id = surveyid,
            user_id= userid,
        )
        
        # Get the corresponding SurveyGroup instance (assuming one exists)
        survey_group = SurveyGroup.objects.get(survey_id=surveyid)
        
        # Extract trigger times from survey group JSONField
        trigger_times = survey_group.trigger_times
        
  
        # Check if end_time of CompletedSurvey falls within any survey's live period
        for index, trigger_time in trigger_times.items():
            # Convert trigger time to datetime object
            trigger_time_obj = timezone.datetime.strptime(trigger_time, "%H:%M").time()

            print(trigger_time_obj)
            
            # Calculate survey start and end times based on trigger time and survey_time
            survey_start_time = timezone.datetime.combine(timezone.now().date(), trigger_time_obj)
            survey_end_time = survey_start_time + timezone.timedelta(minutes=survey.survey_time)
            
            
            for completed_survey in completed_surveys:

                completed_date_time = timezone.datetime.combine(completed_survey.date, completed_survey.end_time)
                # print(f"survey_end_datetime type: {type(survey_end_time)}") 
                # print(f"comlpeted_survey type: {type(survey_end_datetime)}") 
                # Check if end_time of CompletedSurvey is between survey_start_time and survey_end_time
                if survey_start_time <= completed_date_time <= survey_end_time:
                    return True
        
        return False