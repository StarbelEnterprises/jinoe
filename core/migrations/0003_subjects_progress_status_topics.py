# Generated by Django 4.0.6 on 2022-07-09 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_modules_options_alter_modules_table_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='progress_status',
            field=models.CharField(blank=True, choices=[('d', 'Draft'), ('p', 'Published')], max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subjects')),
            ],
        ),
    ]