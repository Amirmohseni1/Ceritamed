from django.contrib import admin

# Register your models here.
from .models import Slider, Partners, Customers, HomeData


def make_published(modeladmin, request, queryset):
    queryset.update(active=True)


make_published.short_description = "فعال کردن اسلایدر"


def make_draft(modeladmin, request, queryset):
    queryset.update(active=False)


make_draft.short_description = "غیره فعال کردن اسلایدر"


class SliderAdmin(admin.ModelAdmin):
    list_display = ("__str__", "active", "category")
    actions = [make_published, make_draft]


admin.site.register(Slider, SliderAdmin)



def make_published(modeladmin, request, queryset):
    queryset.update(active=True)


make_published.short_description = "فعال کردن پارتنر"


def make_draft(modeladmin, request, queryset):
    queryset.update(active=False)


make_draft.short_description = "غیره فعال کردن پارتنر"


class PartnersAdmin(admin.ModelAdmin):
    list_display = ("__str__", "active")
    actions = [make_published, make_draft]


admin.site.register(Partners, PartnersAdmin)



def make_published(modeladmin, request, queryset):
    queryset.update(active=True)


make_published.short_description = "فعال کردن نظر مشتری ها"


def make_draft(modeladmin, request, queryset):
    queryset.update(active=False)


make_draft.short_description = "غیره فعال کردن نظر مشتری ها"


class CustomersAdmin(admin.ModelAdmin):
    list_display = ("__str__", "active")
    actions = [make_published, make_draft]


admin.site.register(Customers, CustomersAdmin)



def make_published(modeladmin, request, queryset):
    queryset.update(active=True)


make_published.short_description = "فعال کردن نظر امار ها"


def make_draft(modeladmin, request, queryset):
    queryset.update(active=False)


make_draft.short_description = "غیره فعال کردن امار ها"


class HomeDataAdmin(admin.ModelAdmin):
    list_display = ("__str__", "active")
    actions = [make_published, make_draft]


admin.site.register(HomeData, HomeDataAdmin)
