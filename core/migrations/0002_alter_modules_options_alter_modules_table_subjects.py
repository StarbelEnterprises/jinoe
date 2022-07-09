# Generated by Django 4.0.6 on 2022-07-09 10:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modules',
            options={'verbose_name_plural': 'Level Modules'},
        ),
        migrations.AlterModelTable(
            name='modules',
            table='jinoe_level_modules',
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, null=True)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('subject_type', models.CharField(blank=True, max_length=60, null=True)),
                ('updated_at', models.DateField(default=datetime.datetime.now)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sbj_created_by', to=settings.AUTH_USER_MODEL)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modules')),
            ],
            options={
                'verbose_name_plural': 'Module Subjects',
                'db_table': 'jinoe_module_subjects',
            },
        ),
    ]
