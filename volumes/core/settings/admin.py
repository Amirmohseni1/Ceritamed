from django.contrib import admin

from .models import Setting, Slider, PartnerCompany, FeedBack


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    pass


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass


@admin.register(PartnerCompany)
class PartnerCompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    pass
