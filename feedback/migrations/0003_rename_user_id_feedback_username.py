# Generated by Django 4.2.6 on 2023-11-23 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedback_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='user_id',
            new_name='username',
        ),
    ]
