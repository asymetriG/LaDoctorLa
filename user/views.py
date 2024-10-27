from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from .models import Patient,Doctor,Admin
from appointment.models import Appointment
from django.contrib import messages
from appointment.views import tıp_branşları


import hashlib,datetime

def get_doctor(request):
    doctor = Doctor.objects.get(doctorID=request.session["doctor_id"])
    print(doctor.name)
    return HttpResponse(doctor.name + " " + doctor.surname)

def index(request):
    return render(request,"index.html")


def is_user(request):
    if "patient_id" not in request.session:
        messages.warning(request,"Bu sayfayı görüntülemek için yetkiniz yok")


def user_register(request):
    
    if request.method=="POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("emailhead") + "@" + request.POST.get("emailbottom")
        username = request.POST.get("username")
        password = hashlib.sha256(request.POST.get("password").encode()).hexdigest()
        birthdate = request.POST.get("birthdate")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        
        if Patient.objects.filter(username=username).exists():
            messages.add_message(request, 50, 'Bu kullanıcı adı zaten alınmış.')
            return redirect(reverse('user_register'))  

        
        new_patient = Patient(
            name=name,
            surname=surname,
            email=email,
            username=username,
            password=password,
            birthdate=birthdate,
            gender=gender,
            phone=phone,
            address=address
        )
        
        new_patient.save()
        messages.success(request,'Kullanıcı başarıyla oluşturuldu')
        return redirect(reverse('index'))  
        
    return render(request,"user_register.html")



def user_login(request):
    if request.method=="POST":
        email = request.POST.get("email")
        password = hashlib.sha256(request.POST.get("password").encode()).hexdigest()
        
        if Patient.objects.filter(email=email,password=password).exists():
            
            patient = Patient.objects.get(email=email,password=password)
            request.session['patient_id'] = patient.patientID
            
            request.session['logged_in'] = True
            patient.is_active = True
            patient.save()
            messages.success(request,"Başarıyla giriş yaptınız.")
            return redirect("index")
        else:
            messages.add_message(request, 50, 'Email veya şifre hatalı')
            return redirect(reverse("user_login"))
        
    return render(request,"login.html")
        
  
  
def doctor_register(request):
    
    if request.method=="POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("emailhead") + "@" + request.POST.get("emailbottom")
        username = request.POST.get("username")
        password = hashlib.sha256(request.POST.get("password").encode()).hexdigest()
        birthdate = request.POST.get("birthdate")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        department = request.POST.get("department")
        hospital = request.POST.get("hospital")
        
        if Doctor.objects.filter(username=username).exists():
            messages.add_message(request, 50, 'Bu kullanıcı adı zaten alınmış.')
            return redirect(reverse('doctor_register'))  

        
        new_patient = Doctor(
            name=name,
            surname=surname,
            email=email,
            username=username,
            password=password,
            birthdate=birthdate,
            gender=gender,
            phone=phone,
            address=address,
            department=department,
            hospital=hospital
        )
        
        new_patient.save()
        messages.success(request,'Kullanıcı başarıyla oluşturuldu')
        return redirect(reverse('index'))  
        
    return render(request,"doctor_register.html")

      
        
def doctor_login(request):
    if request.method=="POST":
        email = request.POST.get("email")
        password = hashlib.sha256(request.POST.get("password").encode()).hexdigest()
        
        if Doctor.objects.filter(email=email,password=password).exists():
            
            doctor = Doctor.objects.get(email=email,password=password)
            request.session['doctor_id'] = doctor.doctorID
            request.session['logged_in'] = True
            
            doctor.is_active = True
            doctor.save()
            messages.success(request,"Başarıyla giriş yaptınız.")
            return redirect("index")
        else:
            messages.add_message(request, 50, 'Email veya şifre hatalı')
            return redirect(reverse("doctor_login"))

        
        
    return render(request,"login.html")



def admin_login(request):
    if request.method=="POST":
        email = request.POST.get("email")
        password = hashlib.sha256(request.POST.get("password").encode()).hexdigest()
        
        if Admin.objects.filter(email=email,password=password).exists():
            admin = Admin.objects.get(email=email,password=password)
            request.session['admin_id'] = admin.adminID
            request.session['logged_in'] = True
            
            admin.is_active = True
            admin.save()
            messages.success(request,"Başarıyla giriş yaptınız.")
            return redirect("index")
        else:
            messages.add_message(request, 50, 'Email veya şifre hatalı')
            return redirect(reverse("admin_login"))

        
        
    return render(request,"login.html")


def logout(request):
    if "admin_id" in request.session:
        admin = Admin.objects.get(adminID=request.session["admin_id"])
        admin.is_active = False
        admin.save()
        
    elif "doctor_id" in request.session:
        admin = Doctor.objects.get(doctorID=request.session["doctor_id"])
        admin.is_active = False
        admin.save()
        
    elif "patient_id" in request.session:
        admin = Patient.objects.get(patientID=request.session["patient_id"])
        admin.is_active = False
        admin.save()
    request.session.clear()
    
    messages.success(request,"Başarıylan çıkış yabdınız.")
    return redirect("index")


def doctors(request):
    data = Doctor.objects.all()
    return render(request,"doctors.html",{'doctors':data})


def edit_doctor(request,id):
    if request.method=="GET":
        doctor = Doctor.objects.get(doctorID=id)
        
        strtime = doctor.birthdate.strftime("%Y-%m-%d")
        
        br_index = tıp_branşları.index(doctor.department)
        return render(request,"edit_doctor.html",{"doctor":doctor,"br_index":br_index,"birthdate":str(strtime)})

    elif request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        birthdate = request.POST.get("birthdate")
        department = request.POST.get("department")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        
        doctor = Doctor.objects.get(doctorID=id)
        doctor.name = name
        doctor.surname = surname
        doctor.birthdate = birthdate
        doctor.department = department
        doctor.phone = phone
        doctor.address = address
        
        doctor.save()
        
        messages.success(request,"Doktor Başarıyla Güncellendi")
        return redirect("dashboard")   
        
        


def dashboard(request):
    
    data = Doctor.objects.all()
    admins = Admin.objects.all()
    mt = False
    
    if len(data)>6:
        data = data[:6]
        mt = True
        
    
    return render(request,"dashboard.html",{'data':data,'mt':mt,"admins":admins})



def doctor_profile(request):
    
    
    
    doctor = Doctor.objects.get(doctorID=request.session['doctor_id'])
    
    appointments = Appointment.objects.filter(doctor=doctor,is_taken=True)
    
    for i in appointments:
        print(i.patient.gender)
        
    return render(request, 'doctor_profile.html',{"doctor":doctor,"apps":appointments})


def admin_register(request):
    
    if request.method=="POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("emailhead") + "@" + request.POST.get("emailbottom")
        username = request.POST.get("username")
        password = hashlib.sha256(request.POST.get("password").encode()).hexdigest()
        birthdate = request.POST.get("birthdate")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        
        if Admin.objects.filter(username=username).exists():
            messages.add_message(request, 50, 'Bu kullanıcı adı zaten alınmış.')
            return redirect(reverse('admin_register'))  

        
        new_admint = Admin(
            name=name,
            surname=surname,
            email=email,
            username=username,
            password=password,
            birthdate=birthdate,
            gender=gender,
            phone=phone,
            address=address
        )
        
        new_admint.save()
        messages.success(request,'Admin başarıyla oluşturuldu')
        return redirect(reverse('index'))  
        
    return render(request,"admin_register.html")


def admin_delete(request,id):
    admin = Admin.objects.get(adminID=id)
    admin.delete()
    
    messages.success(request,"Admin başarıylan silindi.")
    return redirect(reverse('dashboard'))

def doctor_delete(request,id):
    doctor = Doctor.objects.get(doctorID=id)
    
    apps = Appointment.objects.filter(doctor=doctor,is_taken=1)
    
    if apps.exists():
        messages.info(request,"Bu doktorun randevusu olduğu için silemen.")
        return redirect(reverse("dashboard"))
    
    else:
        doctor.delete()
    
        messages.success(request,"Doktor Silindi.")
        return redirect(reverse("dashboard"))
