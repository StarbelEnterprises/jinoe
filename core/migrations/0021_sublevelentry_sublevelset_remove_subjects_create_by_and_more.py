# Generated by Django 4.0.6 on 2022-07-28 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_rename_level_modules_module_level_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubLevelEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, editable=False, null=True)),
                ('name', models.CharField(blank=True, max_length=60)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Eduction Sub Level Set Elements',
                'db_table': 'jinoe_sub_level_set_elements',
            },
        ),
        migrations.CreateModel(
            name='SubLevelSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, editable=False, null=True)),
                ('name', models.CharField(blank=True, max_length=60)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Eduction Sub Level Sets',
                'db_table': 'jinoe_sub_level_set',
            },
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='create_by',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='subject_module_id',
        ),
        migrations.AddField(
            model_name='modules',
            name='progress_status',
            field=models.CharField(choices=[('NST', 'Not_Started'), ('ST', 'Started'), ('DL', 'Delayed'), ('CMP', 'Completed')], default='NST', max_length=30),
        ),
        migrations.AlterField(
            model_name='topics',
            name='topic_subject_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='topic_subject_id_col', to='core.modules'),
        ),
    ]
