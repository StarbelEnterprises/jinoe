# Generated by Django 4.0.6 on 2022-07-10 20:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_subtopics_options_alter_topics_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interactive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, null=True)),
                ('like', models.BooleanField()),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_like_created_by', to=settings.AUTH_USER_MODEL)),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.topics')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Topic Likes',
                'db_table': 'jinoe_user_topic_likes',
            },
        ),
    ]
