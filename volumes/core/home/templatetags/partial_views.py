from django import template
from Articles.models import Article
from contact.forms import NewsLettersForm
from contact.models import Newsletters
from services.models import Service, ServiceCategory

register = template.Library()


@register.inclusion_tag('share/footer.html', takes_context=True)
def footer(context):
    request = context['request']
    blog_data = Article.objects.get_queryset().filter(is_active=True).order_by('-id')[:6]
    service_data = Service.object.get_queryset().filter(active=True).order_by('-id')[:6]
    service_category_data = ServiceCategory.objects.get_queryset().all().order_by('-id')[:6]

    news_letter_form = NewsLettersForm(request.POST or None)
    if news_letter_form.is_valid():
        email = news_letter_form.cleaned_data.get('email')
        Newsletters.objects.create(email=email)
        news_letter_form: NewsLettersForm = NewsLettersForm()

    return {
        'Articles': blog_data,
        'Servise': service_data,
        'ServiseCategory': service_category_data,
        'Forms': news_letter_form,
    }


@register.inclusion_tag('share/header.html', takes_context=True)
def header(context):
    return {}
