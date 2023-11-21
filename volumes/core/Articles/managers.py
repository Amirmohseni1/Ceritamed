from django.db import models


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, is_deleted=False)

    def get_active_list(self):
        return self.all()

    def get_active_list_by_category(self, category):
        return self.filter(category=category)

    def get_by_search(self, query):
        lookup = (models.Q(title__icontains=query))
        return self.get_queryset().filter(lookup).distinct()
    
    
    
class ArticleCategoryManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, is_deleted=False)
    
    def get_active_list(self):
        return self.all()