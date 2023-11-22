from django.views.generic import TemplateView

from contact.forms import ContactUsModelForms
from doctors.models import Doctor
from services.models import ServiceCategory
from settings.models import Slider, FeedBack, PartnerCompany


class Index(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['sliders'] = Slider.objects.all()
        context['partners'] = PartnerCompany.objects.all()
        context['doctors'] = Doctor.objects.all()
        context['services'] = ServiceCategory.objects.all()
        context['customers'] = FeedBack.objects.all()
        return context


class AboutUs(TemplateView):
    template_name = 'home/about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['partners'] = PartnerCompany.objects.all()


class ContactUs(TemplateView):
    template_name = 'home/contact-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = ContactUsModelForms
        return context
