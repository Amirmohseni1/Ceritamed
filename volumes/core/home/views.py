from django.contrib import messages
from django.shortcuts import render

from contact.forms import ContactUsModelForms
from doctors.models import Doctor
from services.models import Service, ServiceCategory
from settings.models import Slider, Partners, Customers, HomeData


def home_page(request):
    sliders = Slider.objects.get_queryset().filter(active=True).order_by('-id')[:5]
    partner = Partners.objects.get_queryset().filter(active=True).order_by("-id")
    doctor_section = Doctor.objects.get_queryset().filter(home_page=True).order_by('-id')[:10]
    service = Service.object.get_queryset().filter(active_home=True).order_by('-id')[:6]
    service_category = ServiceCategory.objects.get_queryset().filter(active_home=True).order_by('-id')[:4]
    customer = Customers.objects.get_queryset().filter(active=True).order_by('-id')
    home_data = HomeData.objects.get_queryset().filter(active=True)[:4]

    context = {
        'service': service,
        "slider": sliders,
        "Doctor_section": doctor_section,
        'Servise_categor': service_category,
        'partners': partner,
        'customer': customer,
        'Home_datas': home_data
    }
    return render(request, "home/index.html", context)


def about_us(request):
    data = HomeData.objects.get_queryset().filter(active=True).order_by('-id')[:4]
    partner = Partners.objects.get_queryset().filter(active=True).order_by('-id')

    context = {
        'data': data,
        'partners': partner,
    }
    return render(request, "home/about-us.html", context)


def contact(request):
    contact_us_form = ContactUsModelForms(request.POST or None)
    if contact_us_form.is_valid():
        contact_us_form.save()
        messages.success(request, 'لقد تم إرسال إستمارتک بعنوان {} بنجاح '.format(contact_us_form.cleaned_data.get('subject')))
        contact_us_form: ContactUsModelForms = ContactUsModelForms()

    context = {
        'contact_us_form': contact_us_form,
    }
    return render(request, "home/contact-us.html", context)
