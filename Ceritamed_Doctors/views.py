from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages

# from Ceritamed_Forms.forms import DoctorsPageForm
from .models import Doctor


# Create your views here.

# --------------------------------------------------- Doctor ListView --------------------------------------------------------

class DoctorsListView(ListView):
    template_name = "Doctors/Doctors_list.html"
    paginate_by = 12

    def get_queryset(self):
        return Doctor.objects.get_queryset().filter(active=True).order_by('-id').only('doctor_name', 'doctor_img',
                                                                                      'doctor_evidence',
                                                                                      'doctor_expertise')


# --------------------------------------------------- Doctor DetailView --------------------------------------------------------

def doctors_detail(request, slug):
    doctors: Doctor = get_object_or_404(Doctor, slug=slug, active=True)

    context = {
        'doctors': doctors,
    }
    return render(request, 'Doctors/Doctors_Detail.html', context)
