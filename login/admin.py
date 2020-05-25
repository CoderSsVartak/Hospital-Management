from django.contrib import admin
from .models import NewUser, Doctor, Patient

admin.site.register(NewUser)
admin.site.register(Doctor)
admin.site.register(Patient)

