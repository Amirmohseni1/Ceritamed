from django.contrib import admin
from .models import Doctor, DoctorExpertise, DoctorEvidence


# Register your models here.

# --------------------------------------------------- Doctors --------------------------------------------------------

class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'home_page', 'active')
    list_filter = ('home_page', 'active')
    search_fields = ('doctor_name', 'slug')


admin.site.register(Doctor, DoctorsAdmin)

# --------------------------------------------------- Doctor Expertise --------------------------------------------------------

admin.site.register(DoctorExpertise)

# --------------------------------------------------- Doctor Evidence --------------------------------------------------------

admin.site.register(DoctorEvidence)
