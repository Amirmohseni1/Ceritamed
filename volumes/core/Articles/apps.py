from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArticleConfig(AppConfig):
    name = 'Articles'
    verbose_name = _('Articles')
