# Generated by Django 4.1.7 on 2023-09-23 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_day_remove_schedule_days_schedule_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='days',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.AddField(
            model_name='schedule',
            name='days',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
