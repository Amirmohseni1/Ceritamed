from django.contrib import admin
from imagekit.admin import AdminThumbnail

from .models import Post, PostCategory, PostComment


# Register your models here.

# --------------------------------------------------- Blog  --------------------------------------------------------
def make_published(modeladmin, request, queryset):
    queryset.update(active=True)


make_published.short_description = "منتشر کردن مقالات"


def make_draft(modeladmin, request, queryset):
    queryset.update(active=False)


make_draft.short_description = "پیش نویس کردن مقالات"


class BlogAdmin(admin.ModelAdmin):
    list_display = ( "__str__", 'blog_views', 'publish', 'update', 'active',)
    list_filter = ('active', 'publish', 'update', 'b_category')
    search_fields = ('title', 'slug', 'descriptions',)
    date_hierarchy = 'publish'
    exclude = ('blog_views',)
    ordering = ['-publish']
    actions = [make_published, make_draft]


admin.site.register(Post, BlogAdmin)


# --------------------------------------------------- Blog Tag --------------------------------------------------------

def make_published(modeladmin, request, queryset):
    queryset.update(active=True)


make_published.short_description = "منتشر کردن کامنت ها"


def make_draft(modeladmin, request, queryset):
    queryset.update(active=False)


make_draft.short_description = "پیش نویس کردن کامنت ها"


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'blog_post', 'email', 'created', 'active')
    list_editable = ('active',)
    list_filter = ('blog_post', 'created', 'active')
    search_fields = ('blog_post', 'email', 'text',)
    date_hierarchy = 'created'
    ordering = ['-created']
    actions = [make_published, make_draft]


admin.site.register(PostComment, BlogCommentAdmin)


# --------------------------------------------------- Blog Category --------------------------------------------------------

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    search_fields = ('title',)


admin.site.register(PostCategory, BlogCategoryAdmin)
