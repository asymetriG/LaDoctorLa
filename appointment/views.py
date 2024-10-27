from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from tqdm import tqdm
from faker import Faker
from user.models import Patient,Doctor,Admin
from django.contrib import messages
from datetime import datetime, timedelta,date
import random

tıp_branşları = [
    "Anatomi",
    "Biyofizik",
    "Tıbbi Biyoloji",
    "Tıp Eğitimi",
    "Tıp Etiği ve Tıp Tarihi",
    "İmmünoloji",
    "Fizyoloji",
    "Histoloji ve Embriyoloji",
    "Tıbbi Mikrobiyoloji",
    "Tıp Bilişimi",
    "Tıbbi Biyokimya",
    "Dahili Tıp Bilimleri",
    "Acil Tıp",
    "Adli Tıp",
    "Çocuk Ruh Sağlığı",
    "Çocuk Sağlığı ve Hastalıkları",
    "Dermatoloji",
    "Enfeksiyon Hastalıkları",
    "Fiziksel Tıp ve Rehabilitasyon",
    "Göğüs Hastalıkları",
    "Halk Sağlığı",
    "İç Hastalıkları",
    "Kardiyoloji",
    "Nöroloji",
    "Nükleer Tıp",
    "Radyasyon Onkolojisi",
    "Radyoloji",
    "Psikiyatri",
    "Tıbbi Farmakoloji",
    "Tıbbi Genetik",
    "Cerrahi Tıp Bilimleri",
    "Anestezi ve Reanimasyon",
    "Beyin ve Sinir Cerrahisi",
    "Çocuk Cerrahisi",
    "Genel Cerrahi",
    "Kalp ve Damar Cerrahisi",
    "Göğüs Cerrahisi",
    "Göz Hastalıkları",
    "Kadın Hastalıkları ve Doğum",
    "Kulak Burun Boğaz",
    "Ortopedi ve Travmatoloji",
    "Tıbbi Patoloji",
    "Üroloji",
    "Plastik Rekonstrüktif ve Estetik Cerrahi"
]


from .models import Appointment

clocks = ["08.00","09.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00"]

def create_doctors(request):
    
    if "admin_id" in request.session:
            
        fake = Faker()
        
        for brans in tıp_branşları:
            for i in range(2):
                name = fake.first_name()
                surname = fake.last_name()
                email = fake.email()
                username = fake.user_name()
                password = "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
                birthdate = "1972-02-02"
                phone = fake.phone_number()
                gender = "Erkek"
                address = fake.address()
                department = brans
                hospital = "LaDoctor"
                
                dr = Doctor(name=name,surname=surname,email=email,username=username,password=password,birthdate=birthdate,phone=phone,gender=gender,address=address,department=department,hospital=hospital)
                dr.save()
            
    return render(request,"index.html")

def create_appointments(request):
    if "admin_id" in request.session:
        print("adminiz")
        start_date = datetime(2024, 5, 1)
        end_date = datetime(2024, 12, 31)
        
        patient = Patient(name="fake",surname="fake",username="fake",email="fake@gmail.com",password="fake",birthdate="2024-02-02",gender="fake",phone="fake",address="fake")
        patient.save()
               
        doctors = Doctor.objects.all()
        
        current_date = start_date
        while current_date <= end_date:
            for clock in clocks:
                for doctor in doctors:
                    appointment_date = current_date.strftime('%Y-%m-%d')
                    appointment_date = datetime.strptime(appointment_date, '%Y-%m-%d').date()
                    
                    app = Appointment(appointment_date=appointment_date,appointment_time=clock,appointment_details="",granted=False,is_taken=False,doctor=doctor,patient=patient)
                    app.save()
            current_date += timedelta(days=1)
                    
    return render(request,"index.html")


def get_appointment(request):
    patient = Patient.objects.get(patientID=request.session["patient_id"])
    strtime = patient.birthdate.strftime("%Y-%m-%d")
    today = datetime.today()
    today = today.strftime("%Y-%m-%d")
    
    if request.method=="GET":    
        
        return render(request,"get_appointment.html",{'patient':patient,"birthdate":str(strtime),"today":today})
    
    if request.method=="POST":
        clock = request.POST.get("time")

        details = request.POST.get("details")

        doctors = Doctor.objects.filter(department=request.POST.get("department"))

        appointments = Appointment.objects.filter(doctor__in=doctors, appointment_time=clock, appointment_date=request.POST.get("appointment_date"),is_taken=0)
        
        request.session["details"] = request.POST.get("details")
        
        return render(request,"get_appointment.html",{"info":appointments,'patient':patient,"birthdate":str(strtime),"today":today})
    
    
    
def appointment(request,id):
    
    patient = Patient.objects.get(patientID=request.session["patient_id"])
    
    if request.method=="GET":
        
        _appointment = Appointment.objects.get(appointmentID=id)
        
        if _appointment.is_taken == 0:
        
            _appointment.appointment_details = request.session["details"]
            _appointment.is_taken = 1
            _appointment.patient = patient
            
            _appointment.save()
            
            request.session.pop("details")
            
            messages.success(request,"Randevu Başarıyla Alındı")
            return redirect("index")
        else:
            messages.info(request,"Randevu Alınamadı")
            return render(request,"appointment.html")


def my_appointments(request):
    
    patient = Patient.objects.get(patientID=request.session["patient_id"])
    
    appointments = Appointment.objects.filter(patient=patient)
    
    return render(request,"my_appointments.html",{"appointments":appointments})