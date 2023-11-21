from django import template
from ..models import ArticleCategory, Article

register = template.Library()


@register.inclusion_tag('blog/components/search.html')
def search():
    return {}


@register.inclusion_tag('blog/components/last_posts.html')
def last_posts():
    articles = Article.custom_objects.get_active_list()[:4]
    return {'articles': articles}


@register.inclusion_tag('blog/components/category.html')
def category():
    categories = ArticleCategory.custom_objects.get_active_list()
    return {'categories': categories}
