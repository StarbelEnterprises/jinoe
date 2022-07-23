# Generated by Django 4.0.6 on 2022-07-23 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0016_merge_20220720_0702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modules',
            name='level',
        ),
        migrations.CreateModel(
            name='SubLevelSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, editable=False, null=True)),
                ('name', models.CharField(blank=True, max_length=60)),
                ('updated_at', models.DateField(auto_now=True)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stlv_created_by', to=settings.AUTH_USER_MODEL)),
                ('sub_level_set_level_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_level_set_level_id_col', to='core.levels')),
            ],
            options={
                'verbose_name_plural': 'Eduction Sub Level Sets',
                'db_table': 'jinoe_sub_level_set',
            },
        ),
        migrations.CreateModel(
            name='SubLevelEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, editable=False, null=True)),
                ('name', models.CharField(blank=True, max_length=60)),
                ('updated_at', models.DateField(auto_now=True)),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stlv_entry_created_by', to=settings.AUTH_USER_MODEL)),
                ('sub_level_entry_set_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_level_entry_set_id_col', to='core.sublevelset')),
            ],
            options={
                'verbose_name_plural': 'Eduction Sub Level Set Elements',
                'db_table': 'jinoe_sub_level_set_elements',
            },
        ),
        migrations.AddField(
            model_name='modules',
            name='module_sub_level_entry_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='module_set', to='core.sublevelentry'),
        ),
    ]
