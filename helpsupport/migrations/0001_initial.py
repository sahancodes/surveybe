# Generated by Django 4.2.6 on 2023-11-15 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('faq_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=150)),
                ('answer', models.CharField(max_length=500)),
                ('category', models.CharField(choices=[('SVY', 'Survey'), ('APP', 'Application'), ('LNG', 'Language'), ('RNK', 'Rank'), ('ACT', 'Account'), ('NOT', 'Notifications')], default='APP', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('SVY', 'Survey'), ('APP', 'Application'), ('LNG', 'Language'), ('RNK', 'Rank'), ('ACT', 'Account'), ('NOT', 'Notifications')], default='APP', max_length=3)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.account')),
            ],
        ),
    ]
