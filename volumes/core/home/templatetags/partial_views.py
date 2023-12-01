from django import template
from Articles.models import Article
from contact.forms import NewsLettersForm
from contact.models import Newsletters
from services.models import Service, ServiceCategory

register = template.Library()


@register.inclusion_tag('share/footer.html', takes_context=True)
def footer(context):
    setting = context['setting']
    socials = context['socials']
    articles = Article.custom_objects.get_active_list()[:6]
    # todo= add services and doctor for footer
    return {
        'articles': articles,
        'setting': setting,
        'socials': socials,
    }


@register.inclusion_tag('share/header.html', takes_context=True)
def header(context):
    setting = context['setting']
    socials = context['socials']
    return {
        'setting': setting,
        'socials': socials,
    }
