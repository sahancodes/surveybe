# Generated by Django 4.2.6 on 2023-11-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_account_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='userimg',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
