# Generated by Django 4.0.6 on 2022-07-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]