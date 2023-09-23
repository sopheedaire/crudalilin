from django.db import models

class Schedule(models.Model):
    PROGRAM_CHOICES = [
        ('Strength', 'Strength'),
        ('Cardio', 'Cardio'),
    ]

    routine_name = models.CharField(max_length=255)
    days = models.CharField(max_length=200, blank=True)  # Use a CharField without choices
    time = models.TimeField()
    hours = models.PositiveIntegerField(default=0)
    minutes = models.PositiveIntegerField(default=0)
    program = models.CharField(max_length=10, choices=PROGRAM_CHOICES)

    def __str__(self):
        return self.routine_name
