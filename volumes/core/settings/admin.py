from django.contrib import admin

from .models import Setting, Slider, PartnerCompany, FeedBack


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        base_add_permission = super(SettingAdmin, self).has_add_permission(request)
        if base_add_permission:
            # this part of code for saved only single record for setting app
            count = Setting.objects.all().count()
            if count == 0:
                return True
        return False


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass


@admin.register(PartnerCompany)
class PartnerCompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    pass
