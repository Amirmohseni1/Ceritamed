from .models import Setting, Social


def setting(request):
    setting = Setting.objects.first()
    return {'setting': setting}


def social(request):
    socials = Social.custom_objects.all()
    return {'socials': socials}
