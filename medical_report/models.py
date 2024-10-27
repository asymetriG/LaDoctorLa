from django.db import models
from user.models import Doctor,Patient

class MedicalReport(models.Model):
    reportID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    report_date = models.DateField()
    report_time = models.TimeField()
    report_content = models.TextField()
    URL = models.CharField(max_length=255)

    def __str__(self):
        return f"Medical Report {self.reportID} - {self.patient} - {self.report_date} {self.report_time}"
