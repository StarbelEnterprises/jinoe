# Generated by Django 4.0.6 on 2022-08-07 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_topics_options'),
        ('cariculam_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cariculamsubjects',
            name='Level_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='subjecr_set', to='core.levels'),
        ),
    ]
