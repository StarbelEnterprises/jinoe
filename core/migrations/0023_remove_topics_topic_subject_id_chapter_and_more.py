# Generated by Django 4.0.6 on 2022-07-28 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0022_delete_subjects_sublevelset_create_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topics',
            name='topic_subject_id',
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, editable=False, null=True)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sbj_created_by', to=settings.AUTH_USER_MODEL)),
                ('module_chapter_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='module_chapter_id_col', to='core.modules')),
            ],
            options={
                'verbose_name_plural': 'Module Chapters',
                'db_table': 'jinoe_module_chapters',
            },
        ),
        migrations.AddField(
            model_name='topics',
            name='topic_chapter_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='topic_subject_id_col', to='core.chapter'),
        ),
    ]
