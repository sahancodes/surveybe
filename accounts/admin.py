from django.contrib import admin
from .models import Account, SurveyGroup
from .management.commands.resetlevels import Command as ResetLevels
from django.utils.translation import gettext_lazy as _

# Register your models here.
admin.site.register(SurveyGroup)


class AccountAdmin(admin.ModelAdmin):
    actions = ['reset_contribution_and_level']

    def reset_contribution_and_level(self, request, queryset):
        command = ResetLevels()
        command.handle()

    reset_contribution_and_level.short_description = _("Reset All Levels")

admin.site.register(Account, AccountAdmin)