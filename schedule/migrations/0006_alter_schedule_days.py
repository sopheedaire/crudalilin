# Generated by Django 4.1.7 on 2023-09-23 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_remove_schedule_days_delete_day_schedule_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='days',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
