from django.shortcuts import render
from Ceritamed_Additional_Features.models import Partners, HomeData


# Create your views here.


def about_us(request):
    data: HomeData = HomeData.objects.get_queryset().filter(active=True).order_by('-id')[:4]
    partner: Partners = Partners.objects.get_queryset().filter(active=True).order_by('-id')

    context = {
        'data': data,
        'partners': partner,
    }
    return render(request, "about-us/about-us.html", context)
