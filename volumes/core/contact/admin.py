from django.contrib import admin
from .models import ContactUs, Consultation, Newsletters

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read',)
    search_fields = ('title', 'body', 'subject')


@admin.register(Consultation)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'source', 'is_read', 'created_at')
    list_filter = ('is_read',)
    search_fields = ('title', 'body')


@admin.register(Newsletters)
class NewslettersAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('email',)
