# Generated by Django 4.2.6 on 2024-05-30 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_alter_feedback_timestamp_alter_feedback_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='body',
            field=models.TextField(max_length=2000),
        ),
    ]
