from django.contrib import admin
from Ceritamed_Services.models import ServiceCategory, Service, ServicePrice


# --------------------------------------------------- Servise Category --------------------------------------------------------

# ------------------------------ Servise Category published / Draft -----------------------------


def make_published(modeladmin, request, queryset):
    queryset.update(active=True)


make_published.short_description = "فعال کردن دسته بندی"


def make_draft(modeladmin, request, queryset):
    queryset.update(active=False)


make_draft.short_description = "غیره فعال کردن دسته بندی"


# ------------------------------ Servise Category Home published / Home Draft -----------------------------


def make_published_home(modeladmin, request, queryset):
    queryset.update(active_Home=True)


make_published_home.short_description = "فعال کردن دسته بندی در صفحه اصلی"


def make_draft_Home(modeladmin, request, queryset):
    queryset.update(active_Home=False)


make_draft_Home.short_description = "غیره فعال کردن دسته بندی در صفحه اصلی"


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'active_home', 'active',)
    list_filter = ('active', 'active_home')
    search_fields = ('title', 'slug', 'descriptions',)
    actions = [make_published, make_draft, make_published_home, make_draft_Home]


# --------------------------------------------------- Servise  --------------------------------------------------------


admin.site.register(ServiceCategory, ServiceCategoryAdmin)


# ------------------------------ Servise Category published / Draft -----------------------------

def make_published(modeladmin, request, queryset):
    queryset.update(active=True)


make_published.short_description = "فعال کردن خدمت"


def make_draft(modeladmin, request, queryset):
    queryset.update(active=False)


make_draft.short_description = "غیره فعال کردن خدمت"


# ------------------------------ Servise Home published / Home Draft -----------------------------


def make_published_home(modeladmin, request, queryset):
    queryset.update(active_Home=True)
make_published_home.short_description = "فعال کردن خدمت در صفحه اصلی"


def make_draft_Home(modeladmin, request, queryset):
    queryset.update(active_Home=False)
make_draft_Home.short_description = "غیره فعال کردن خدمت در صفحه اصلی"

class InLineProductPrice(admin.TabularInline):
    model = ServicePrice
    extra = 1


class ServiceAdmin(admin.ModelAdmin):
    inlines = [InLineProductPrice]
    list_display = ("__str__", 'price', 'publish', 'active', 'active_home')
    list_filter = ('active_home', 'active', 'publish', 's_category')
    search_fields = ('title', 'slug', 'descriptions', 'description')
    date_hierarchy = 'publish'
    ordering = ['-publish']
    actions = [make_published, make_draft, make_published_home, make_draft_Home]


admin.site.register(Service, ServiceAdmin)


class ServicePriceAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'price', 'service')
    list_filter = ('service',)
    search_fields = ('name',)

admin.site.register(ServicePrice, ServicePriceAdmin)
