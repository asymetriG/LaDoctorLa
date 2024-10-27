from django.db import models
from user.models import Patient,Doctor

class Appointment(models.Model):
    appointmentID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,default=None)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,default=None)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_details = models.TextField()
    granted = models.BooleanField(default=False)
    is_taken = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Appointment {self.appointmentID} - {self.appointment_date} {self.appointment_time}"
