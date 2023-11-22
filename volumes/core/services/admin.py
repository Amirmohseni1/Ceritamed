from django.contrib import admin
from .models import ServiceCategory, Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'index', 'is_active')
    list_filter = ('is_active', 'index')
    search_fields = ('title',)

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'index', 'is_active', 'is_deleted')
    list_filter = ('index', 'is_active', 'is_deleted')
    search_fields = ('title',)