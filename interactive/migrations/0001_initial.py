# Generated by Django 4.0.6 on 2022-07-10 08:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_alter_subtopics_options_alter_topics_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, null=True)),
                ('stars', models.IntegerField(default=0)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_rate_created_by', to=settings.AUTH_USER_MODEL)),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.topics')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Topic Rates',
                'db_table': 'jinoe_user_topic_rates',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('points', models.IntegerField(default=0)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qn_created_by', to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.topics')),
            ],
            options={
                'verbose_name_plural': 'Topic Questions',
                'db_table': 'jinoe_topic_questions',
            },
        ),
        migrations.CreateModel(
            name='AnswerOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, null=True)),
                ('answer', models.CharField(blank=True, max_length=60, null=True)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ans_opt_created_by', to=settings.AUTH_USER_MODEL)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_options_question', to='interactive.questions')),
            ],
            options={
                'verbose_name_plural': 'Question Answers',
                'db_table': 'jinoe_question_answers',
            },
        ),
        migrations.CreateModel(
            name='AnswerLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, null=True)),
                ('answer_log', models.CharField(blank=True, max_length=60, null=True)),
                ('scores', models.IntegerField(default=0)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ans_log_created_by', to=settings.AUTH_USER_MODEL)),
                ('questin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interactive.questions')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Answer Logs',
                'db_table': 'jinoe_user_answer_logs',
            },
        ),
    ]
