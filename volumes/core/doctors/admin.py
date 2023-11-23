from django.contrib import admin
from .models import Doctor, DoctorExpertise, DoctorEducation


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


@admin.register(DoctorEducation)
class DoctorEducationAdmin(admin.ModelAdmin):
    pass


@admin.register(DoctorExpertise)
class DoctorExpertiseAdmin(admin.ModelAdmin):
    pass
