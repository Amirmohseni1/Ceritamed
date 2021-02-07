from django.conf import settings
from django.utils import translation
from django.http import HttpResponseRedirect


def AdminLocaleMiddleware(get_response):
    def middleware(request):
        if request.path.startswith('/django-admin'):
            request.LANG = getattr(settings, 'ADMIN_LANGUAGE_CODE',
                                   settings.LANGUAGE_CODE)
            translation.activate(request.LANG)
            request.LANGUAGE_CODE = request.LANG

        response = get_response(request)

        return response

    return middleware
