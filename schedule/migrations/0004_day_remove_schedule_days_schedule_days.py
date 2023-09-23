# Generated by Django 4.1.7 on 2023-09-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_alter_schedule_program_delete_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='days',
        ),
        migrations.AddField(
            model_name='schedule',
            name='days',
            field=models.ManyToManyField(to='schedule.day'),
        ),
    ]