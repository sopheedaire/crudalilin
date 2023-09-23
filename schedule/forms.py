from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['routine_name', 'days', 'time', 'hours', 'minutes', 'program']


    DAYS_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    days = forms.MultipleChoiceField(
        choices=DAYS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        required=True,  # Adjust this as needed
    )
    hours = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'number', 'class': 'modern-number-input'}),
        required=True,  # Adjust this as needed
    )

    minutes = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'number', 'class': 'modern-number-input'}),
        required=True,  # Adjust this as needed
    )


    def clean_days(self):
        selected_days = self.cleaned_data.get('days', [])
        return ','.join(selected_days)
