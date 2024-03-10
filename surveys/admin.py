from django.contrib import admin
from .models import Survey, Question, Answer, CompletedSurvey
from django.utils.translation import gettext_lazy as _
from .management.commands.reset_answer_table import Command as ResetAnswerTableCommand
from .management.commands.reset_question_table import Command as ResetQuestionTableCommand


# # Register your models here.
admin.site.register(Survey)
admin.site.register(CompletedSurvey)


class QuestionAdmin(admin.ModelAdmin):
    actions = ['reset_question_table']

    def reset_question_table(self, request, queryset):
        command = ResetQuestionTableCommand()
        command.handle()

    reset_question_table.short_description = _("Reset Table and Delete All Entries")

admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    actions = ['reset_answer_table']

    def reset_answer_table(self, request, queryset):
        command = ResetAnswerTableCommand()
        command.handle()

    reset_answer_table.short_description = _("Reset Table and Delete All Entries")

admin.site.register(Answer, AnswerAdmin)