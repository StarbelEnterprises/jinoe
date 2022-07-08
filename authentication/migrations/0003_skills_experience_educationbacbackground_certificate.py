# Generated by Django 4.0.6 on 2022-07-08 14:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0002_remove_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, null=True)),
                ('skills', models.TextField(null=True)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skl_created_by', to=settings.AUTH_USER_MODEL)),
                ('entery_level_profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills_entery_level_profile', to='authentication.userprofile')),
            ],
            options={
                'verbose_name_plural': 'user skills',
                'db_table': 'jinoe_user_skills',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, null=True)),
                ('experience', models.TextField(null=True)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exp_created_by', to=settings.AUTH_USER_MODEL)),
                ('entery_level_profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience_entery_level_profile', to='authentication.userprofile')),
            ],
            options={
                'verbose_name_plural': 'user experience',
                'db_table': 'jinoe_user_experience',
            },
        ),
        migrations.CreateModel(
            name='EducationBacbackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, null=True)),
                ('education', models.TextField(null=True)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ed_created_by', to=settings.AUTH_USER_MODEL)),
                ('entery_level_profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education_entery_level_profile', to='authentication.userprofile')),
            ],
            options={
                'verbose_name_plural': 'user education',
                'db_table': 'jinoe_user_education',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, null=True)),
                ('certificate', models.TextField(null=True)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cer_created_by', to=settings.AUTH_USER_MODEL)),
                ('entery_level_profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate_entery_level_profile', to='authentication.userprofile')),
            ],
            options={
                'verbose_name_plural': 'user certificate',
                'db_table': 'jinoe_user_certificate',
            },
        ),
    ]