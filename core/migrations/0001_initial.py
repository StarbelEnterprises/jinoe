# Generated by Django 4.0.6 on 2022-07-08 16:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0003_skills_experience_educationbacbackground_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, null=True)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lv_created_by', to=settings.AUTH_USER_MODEL)),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.userprofile')),
            ],
            options={
                'verbose_name_plural': 'user Levels',
                'db_table': 'jinoe_user_Levels',
            },
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, null=True)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='md_created_by', to=settings.AUTH_USER_MODEL)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.levels')),
            ],
            options={
                'verbose_name_plural': 'User Modules',
                'db_table': 'jinoe_user_modules',
            },
        ),
    ]
