from django.db import models
# from django.conf import settings
from accounts.models import Account

# Create your models here.
class Schedule(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    day = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    

    def __str__(self):
        return self.user.email

class Appointment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    condition = models.CharField(max_length=100)
