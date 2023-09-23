from django.shortcuts import render, redirect
from .forms import ScheduleForm
from .models import Schedule

def sched(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show_schedules')  # Use the URL name here
            except:
                pass
    else:
        form = ScheduleForm()
    return render(request, 'schedule/index.html', {'form': form})  # Specify the app name

def show(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedule/show.html', {'schedules': schedules})  # Specify the app name

def edit(request, id):
    schedule = Schedule.objects.get(id=id)
    if request.method == "POST":
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            # Save the updated schedule
            form.save()
            return redirect('show_schedules')  # Redirect to the 'show_schedules' view after updating
    else:
        # Initialize the form with the instance data
        form = ScheduleForm(instance=schedule)

        # Convert the selected days to a list if they are stored as a comma-separated string
        selected_days = schedule.days.split(',') if schedule.days else []

        # Set initial values for the 'days' field to preselect the checkboxes
        form.initial['days'] = selected_days
    
    return render(request, 'schedule/edit.html', {'form': form})


def update(request, id):
    schedule = Schedule.objects.get(id=id)
    form = ScheduleForm(request.POST, instance=schedule)
    if form.is_valid():
        form.save()
        return redirect('show_schedules')  # Redirect to the 'show_schedules' view after updating


def destroy(request, id):
    schedule = Schedule.objects.get(id=id)
    schedule.delete()
    return redirect('show_schedules')  # Use the URL name here
