from django.shortcuts import render
from user.views import Doctor
from .models import MessageSharing



# Create your views here.
def active_doctors(request):
    
    active_doctors = Doctor.objects.filter(is_active=True)
    print(active_doctors)
    
    if(len(active_doctors)==0):
    
        return render(request,"active_doctor.html",{"is_active_doctor":False})
    
    else:
        return render(request,"active_doctor.html",{"is_active_doctor":True,"active_doctors":active_doctors})
    
    
def send_message(request,reciever_id):
    myDoctor = Doctor.objects.get(doctorID=request.session["doctor_id"])
    targetDoctor = Doctor.objects.get(doctorID=reciever_id)
    all_mesages = MessageSharing.objects.filter(sender_doctor=myDoctor,receiver_doctor=targetDoctor)
    
    
    
    return render(request,"messaging.html",{"all_messages":all_mesages})