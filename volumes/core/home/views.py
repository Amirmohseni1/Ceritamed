from django.views.generic import TemplateView

from contact.forms import ContactUsModelForms
from doctors.models import Doctor
from services.models import Service, ServiceCategory
from settings.models import Slider, Partners, Customers, HomeData


class Index(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['sliders'] = Slider.objects.get_queryset().filter(active=True).order_by('-id')[:5]
        context['partners'] = Partners.objects.get_queryset().filter(active=True).order_by("-id")
        context['doctors'] = Doctor.objects.get_queryset().filter(home_page=True).order_by('-id')[:10]
        context['services'] = ServiceCategory.objects.get_queryset().filter(active_home=True).order_by('-id')[:4]
        context['customers'] = Customers.objects.get_queryset().filter(active=True).order_by('-id')
        context['home_data'] = HomeData.objects.get_queryset().filter(active=True)[:4]
        return context


class AboutUs(TemplateView):
    template_name = 'home/about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['partners'] = Partners.objects.get_queryset().filter(active=True)


class ContactUs(TemplateView):
    template_name = 'home/contact-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = ContactUsModelForms
        return context
