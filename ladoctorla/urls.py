"""
URL configuration for ofyadjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from user import views as userviews
from appointment import views as appointmentviews
from messagesharing import views as messageviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userviews.index,name="index"),
    path('user_register', userviews.user_register,name="user_register"),
    path('user_login', userviews.user_login,name="user_login"),
    path('doctor_register', userviews.doctor_register,name="doctor_register"),
    path('doctor_login', userviews.doctor_login,name="doctor_login"),
    path('admin_register', userviews.admin_register,name="admin_register"),
    path('get_doctor', userviews.get_doctor,name="get_doctor"),
    path('admin_login', userviews.admin_login,name="admin_login"),
    path('admin_delete/<int:id>/', userviews.admin_delete,name="admin_delete"),
    path('doctor_delete/<int:id>/', userviews.doctor_delete,name="doctor_delete"),
    path('logout', userviews.logout,name="logout"),
    path('dashboard', userviews.dashboard,name="dashboard"),
    path('doctors', userviews.doctors,name="doctors"),
    path('edit_doctor/<int:id>/', userviews.edit_doctor,name="edit_doctor"),
    path('doctor_profile/', userviews.doctor_profile,name="doctor_profile"),
    path('create_appointments', appointmentviews.create_appointments,name="create_appointments"),
    path('create_doctors', appointmentviews.create_doctors,name="create_doctors"),
    path('get_appointment', appointmentviews.get_appointment,name="get_appointment"),
    path('appointment/<int:id>/', appointmentviews.appointment,name="appointment"),
    path('my_appointments', appointmentviews.my_appointments,name="my_appointments"),
    path('active_doctors', messageviews.active_doctors,name="active_doctors"),
    path('send_message/<int:reciever_id>/', messageviews.send_message,name="send_message"),
]
