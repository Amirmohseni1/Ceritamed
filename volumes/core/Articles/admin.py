from django.contrib import admin

from .models import Article, ArticleCategory, ArticleComment, ArticleTag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'visit', 'created_at', 'modified_at', 'is_active')
    list_filter = ('is_active', 'modified_at', 'created_at')
    search_fields = ('title', 'slug', 'body')
    ordering = ['-created_at']
    prepopulated_fields = {'slug': ('title',), }


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('created_at', 'is_active')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    prepopulated_fields = {'slug': ('title',), }



@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'article')
    search_fields = ('title',)


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',), }

