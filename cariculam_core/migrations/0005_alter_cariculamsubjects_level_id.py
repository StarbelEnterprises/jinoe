# Generated by Django 4.0.6 on 2022-08-07 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_topics_options'),
        ('cariculam_core', '0004_remove_cariculamsubjects_module_subject_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cariculamsubjects',
            name='Level_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='subject_set', to='core.enrollment'),
        ),
    ]
