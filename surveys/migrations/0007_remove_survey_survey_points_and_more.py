# Generated by Django 4.2.6 on 2023-11-29 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0006_alter_answer_answers_alter_answer_next_question_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='survey_points',
        ),
        migrations.AlterField(
            model_name='survey',
            name='survey_intro',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
