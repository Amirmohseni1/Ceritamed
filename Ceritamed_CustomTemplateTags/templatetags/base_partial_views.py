from django import template
from Ceritamed_Blog.models import Post
from Ceritamed_Newsletters.forms import NewsLettersForm
from Ceritamed_Newsletters.models import Newsletters
from Ceritamed_Services.models import Service, ServiceCategory

register = template.Library()


# ------------------------------------------------------------ Components tags ------------------------------------------------------


@register.inclusion_tag('Share/_Footer.html', takes_context=True)
def footer(context):
    request = context['request']
    blog_data: Post = Post.object.get_queryset().filter(active=True).order_by('-id')[:6]
    service_data: Service = Service.object.get_queryset().filter(active=True).order_by('-id')[:6]
    service_category_data: ServiceCategory = ServiceCategory.objects.get_queryset().all().order_by('-id')[:6]

    # ----------------------forms------------------------
    news_letter_form: NewsLettersForm = NewsLettersForm(request.POST or None)
    if news_letter_form.is_valid():
        email = news_letter_form.cleaned_data.get('email')
        Newsletters.objects.create(email=email)
        news_letter_form: NewsLettersForm = NewsLettersForm()

    return {
        'blog': blog_data,
        'Servise': service_data,
        'ServiseCategory': service_category_data,
        'Forms': news_letter_form,
    }


@register.inclusion_tag('Share/_Header.html', takes_context=True)
def header(context):
    return {
    }
