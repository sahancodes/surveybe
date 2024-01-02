# Generated by Django 4.2.6 on 2023-11-30 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_account_authtoken'),
        ('surveys', '0009_remove_completedsurvey_survey_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedsurvey',
            name='survey_id',
            field=models.CharField(default=1, max_length=30),
        ),
        migrations.AlterField(
            model_name='completedsurvey',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='accounts.account'),
        ),
    ]
