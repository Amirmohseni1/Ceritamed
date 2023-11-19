from django import template
from ..models import PostCategory, Post

register = template.Library()


@register.inclusion_tag('Blog/components/../templates/Blog/components/search.html')
def search():
    return {}


@register.inclusion_tag('Blog/components/../templates/Blog/components/last_posts.html')
def last_posts():
    posts: Post = Post.object.get_queryset().filter(active=True).order_by('-blog_views')[:4]
    return {
        "posts": posts
    }


@register.inclusion_tag('Blog/components/../templates/Blog/components/category.html')
def category():
    categories: PostCategory = PostCategory.objects.get_queryset().all()
    return {
        'categories': categories
    }
