# Generated by Django 4.2.6 on 2023-12-07 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('level', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('contribution_addition', models.SmallIntegerField()),
                ('lower_limit', models.SmallIntegerField()),
                ('upper_limit', models.SmallIntegerField()),
            ],
        ),
    ]
