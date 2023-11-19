from django.urls import path, include
from .views import blog_list, blog_detail, Search, blog_category

urlpatterns = [
    path('blog', blog_list, name="blog_list"),
    path('blog/<pk>/<slug:slug>', blog_detail, name="blog_detail"),
    path('blog/search', Search.as_view(), name="Search"),
    path('blog/<slug:slug>', blog_category, name="Blog category"),
]
