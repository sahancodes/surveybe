# Generated by Django 4.2.6 on 2024-05-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0014_alter_survey_survey_intro_alter_survey_survey_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='next_question_id',
        ),
        migrations.AddField(
            model_name='answer',
            name='unfoldings',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='isinfirstqset',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='unfoldingsurvey',
            field=models.BooleanField(default=False),
        ),
    ]
