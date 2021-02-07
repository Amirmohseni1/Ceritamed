from django.contrib import admin
from Ceritamed_Forms.models import ContactUsForm, Form


class ContactUsFormAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'full_name', 'email', 'date', 'is_read',)
    list_filter = ('is_read', 'date',)


admin.site.register(ContactUsForm, ContactUsFormAdmin)
admin.site.register(Form)

