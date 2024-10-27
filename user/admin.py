from django.contrib import admin

from .models import Patient,Doctor,Admin

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Admin)

#8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918