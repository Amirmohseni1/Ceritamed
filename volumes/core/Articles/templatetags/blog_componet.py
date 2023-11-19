from django import template
from ..models import ArticleCategory, Article

register = template.Library()


@register.inclusion_tag('blog/components/search.html')
def search():
    return {}


@register.inclusion_tag('blog/components/last_posts.html')
def last_posts():
    posts: Article = Article.custom_objects.get_active_list()[:4]
    return {
        "posts": posts
    }


@register.inclusion_tag('blog/components/category.html')
def category():
    categories: ArticleCategory = ArticleCategory.objects.get_queryset().all()
    return {
        'categories': categories
    }
