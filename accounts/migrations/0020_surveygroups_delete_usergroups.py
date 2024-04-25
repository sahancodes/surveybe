# Generated by Django 4.2.6 on 2024-04-18 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0013_alter_completedsurvey_user_id'),
        ('accounts', '0019_alter_usergroups_group_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyGroups',
            fields=[
                ('group_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('members', models.ManyToManyField(related_name='user_groups', to='accounts.account')),
                ('survey_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='surveys.survey')),
            ],
        ),
        migrations.DeleteModel(
            name='UserGroups',
        ),
    ]