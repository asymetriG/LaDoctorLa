from django.db import models
from user.models import Doctor,Patient



class MessageSharing(models.Model):
    messageID = models.AutoField(primary_key=True)
    sender_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='sent_messages', default=None)
    receiver_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='received_messages', default=None)
    message_content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Appointment {self.messageID} - {self.sender_doctor} {self.reciever_doctor}"