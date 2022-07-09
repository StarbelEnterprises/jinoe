# Generated by Django 4.0.6 on 2022-07-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_subjects_progress_status_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='progress_status',
            field=models.CharField(blank=True, choices=[('ST', 'STARTED'), ('NST', 'NOT_STARTED'), ('DL', 'DELAYED'), ('CMP', 'COMPLETED'), ('DISC', 'DISQUALIFIED')], max_length=30, null=True),
        ),
    ]
