from django.contrib import admin
from .models import Schedule, Appointment

# Register your models here.

admin.site.register(Schedule)

# admin.site.register(AppointmentBooked)

# class ScheduleCustom(admin.ModelAdmin):
#     list_display =(,'day', 'hours')
# admin.site.register(Schedule, ScheduleCustom)

class AppointmentCustom(admin.ModelAdmin):
    list_display =('user','patient_name', 'email', 'phone')
admin.site.register(Appointment, AppointmentCustom)