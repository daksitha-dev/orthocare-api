from django.contrib import admin
from .models import Patient, Treatment, History

# Register your models here.

admin.site.register(Patient)
admin.site.register(Treatment)
admin.site.register(History)
