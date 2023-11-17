from django.shortcuts import render
from apps.doctors.models import Doctor

from apps.services.models import Service, ServiceCategory
from apps.additional_features.models import Slider, Partners, Customers, HomeData



# -------------------------------------


def home_page(request):
    sliders: Slider = Slider.objects.get_queryset().filter(active=True).order_by('-id')[:5]
    partner: Partners = Partners.objects.get_queryset().filter(active=True).order_by("-id")
    doctor_section: Doctor = Doctor.objects.get_queryset().filter(home_page=True).order_by('-id')[:10]
    service: Service = Service.object.get_queryset().filter(active_home=True).order_by('-id')[:6]
    service_category: ServiceCategory = ServiceCategory.objects.get_queryset().filter(active_home=True).order_by('-id')[:4]
    customer: Customers = Customers.objects.get_queryset().filter(active=True).order_by('-id')
    home_data: HomeData = HomeData.objects.get_queryset().filter(active=True)[:4]

    context = {
        'service': service,
        "slider": sliders,
        "Doctor_section": doctor_section,
        'Servise_categor': service_category,
        'partners': partner,
        'customer': customer,
        'Home_datas': home_data
    }
    return render(request, "home_page.html", context)