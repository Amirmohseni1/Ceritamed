from django.shortcuts import render
from .models import Setting


def setting(request):
    setting = Setting.objects.first()
    return {'setting': setting}
