# Generated by Django 4.0.6 on 2022-07-17 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_alter_enrollment_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_to_set', to='core.levels'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_student_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
