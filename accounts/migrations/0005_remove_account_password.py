# Generated by Django 4.2.6 on 2023-11-23 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_account_user_id_account_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
    ]
