from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import ServiceCategory, Service


# --------------------------------------------------- Services_category ListView--------------------------------------------------------


class ServicesCategory(ListView):
    template_name = 'Services/services-category.html'

    def get_queryset(self):
        return ServiceCategory.objects.filter(active=True).order_by('-id')


# --------------------------------------------------- services_list ListView--------------------------------------------------------

def services_list(request, slug):
    services: ServiceCategory = get_object_or_404(ServiceCategory, slug=slug, active=True)
    context = {
        "services": services,
    }
    return render(request, 'Services/services-List.html', context)


# --------------------------------------------------- Services_category DetailView--------------------------------------------------------

def services_detail(request, slug, pk):
    services: Service = get_object_or_404(Service.object.prefetch_related('serviceprice_set'), slug=slug, active=True, id=pk)
    prices: Service = services.serviceprice_set.all()

    context = {
        "services": services,
        'prices': prices

    }
    return render(request, 'Services/services_detail.html', context)
