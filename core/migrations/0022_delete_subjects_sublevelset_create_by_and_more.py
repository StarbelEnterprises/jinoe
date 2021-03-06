# Generated by Django 4.0.6 on 2022-07-28 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_sublevelentry_sublevelset_remove_subjects_create_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedules', '0005_alter_subjectschedules_subject_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subjects',
        ),
        migrations.AddField(
            model_name='sublevelset',
            name='create_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stlv_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sublevelset',
            name='sub_level_set_level_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_level_set_level_id_col', to='core.levels'),
        ),
        migrations.AddField(
            model_name='sublevelentry',
            name='create_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stlv_entry_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sublevelentry',
            name='sub_level_entry_set_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_level_entry_set_id_col', to='core.sublevelset'),
        ),
    ]
