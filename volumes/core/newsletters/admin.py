from django.contrib import admin

# Register your models here.
from .models import Newsletters


class NewslettersAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
    list_filter = ('date',)
    search_fields = ('email',)


admin.site.register(Newsletters, NewslettersAdmin)
