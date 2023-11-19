from django.contrib import admin
from .models import ContactUsForm, Form
from .models import Newsletters


class ContactUsFormAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'full_name', 'email', 'date', 'is_read',)
    list_filter = ('is_read', 'date',)


admin.site.register(ContactUsForm, ContactUsFormAdmin)
admin.site.register(Form)



class NewslettersAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
    list_filter = ('date',)
    search_fields = ('email',)


admin.site.register(Newsletters, NewslettersAdmin)

