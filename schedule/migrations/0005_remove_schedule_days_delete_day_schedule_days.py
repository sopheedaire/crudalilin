# Generated by Django 4.1.7 on 2023-09-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_day_remove_schedule_days_schedule_days'),
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
            field=models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=200),
        ),
    ]
