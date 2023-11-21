from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCategoryListView

app_name = 'Article'
urlpatterns = [
    path('', ArticleListView.as_view(), name="List"),
    path('<slug:slug>/', ArticleDetailView.as_view(), name="Detail"),
    path('<slug:slug>/', ArticleCategoryListView.as_view(), name="Category"),
]
