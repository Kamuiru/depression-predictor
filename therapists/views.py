from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Schedule, Appointment
from .forms import ScheduleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user)
    return render(request, 'therapist/dashboard.html', {'appointments': appointments})



@login_required(login_url='login')
def schedule_view(request):
    user = request.user
    schedules = Schedule.objects.filter(user=user)
    return render(request, 'therapist/index.html', {'schedules': schedules})

@login_required(login_url='login')
def schedule_show(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    return render(request, 'therapist/show.html', {'schedule':schedule})

@login_required(login_url='login')
def schedule_create(request):
    schedule_form = ScheduleForm(request.POST or None)
    if schedule_form.is_valid():
        schedule_form.save()
        return redirect('schedule')
    return render(request, 'therapist/create.html', {'schedule_form':schedule_form})

@login_required(login_url='login')
def schedule_update(request, schedule_id):
    schedule_update = get_object_or_404(Schedule, id=schedule_id)
    schedule_form = ScheduleForm(request.POST or None, instance=schedule_update)
    if schedule_form.is_valid():
        schedule_form.save()
        return redirect('schedule')
    return render(request, 'therapist/update.html', {'schedule_form':schedule_form})

def schedule_delete(request, schedule_id):
    schedule_delete = get_object_or_404(Schedule, id= schedule_id)
    schedule_delete.delete()
    return redirect('schedule')
