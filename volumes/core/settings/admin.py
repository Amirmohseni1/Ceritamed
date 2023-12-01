from django.contrib import admin

from .models import Setting, Slider, PartnerCompany, FeedBack, Social


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        add_permission = super(SettingAdmin, self).has_add_permission(request)
        if add_permission:
            # this part of code for saved only single record for setting app
            count = Setting.objects.all().count()
            if count == 0:
                return True
        return False


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'rank')
    list_editable = ('rank',)
    ordering = ('rank',)

    def save_model(self, request, obj, form, change):
        objects = Slider.objects.all()
        for object in objects:
            if object.rank >= obj.rank and not change:
                object.rank = object.rank + 1
                object.save()
        if change:
            obj_count_before = Slider.objects.get(id=obj.id)
            for object in objects:
                if object.rank > obj_count_before.rank:
                    object.rank -= 1
                    object.save()
                    if object.rank >= obj.rank:
                        object.rank += 1
                        object.save()
        return super().save_model(request, obj, form, change)


@admin.register(PartnerCompany)
class PartnerCompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'rank')
    list_editable = ('rank',)
    ordering = ('rank',)

    def save_model(self, request, obj, form, change):
        objects = PartnerCompany.objects.all()
        for object in objects:
            if object.rank >= obj.rank and not change:
                object.rank = object.rank + 1
                object.save()
        if change:
            obj_count_before = PartnerCompany.objects.get(id=obj.id)
            for object in objects:
                if object.rank > obj_count_before.rank:
                    object.rank -= 1
                    object.save()
                    if object.rank >= obj.rank:
                        object.rank += 1
                        object.save()
        return super().save_model(request, obj, form, change)


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('title', 'rank')
    list_editable = ('rank',)
    ordering = ('rank',)

    def save_model(self, request, obj, form, change):
        objects = FeedBack.objects.all()
        for object in objects:
            if object.rank >= obj.rank and not change:
                object.rank = object.rank + 1
                object.save()
        if change:
            obj_count_before = FeedBack.objects.get(id=obj.id)
            for object in objects:
                if object.rank > obj_count_before.rank:
                    object.rank -= 1
                    object.save()
                    if object.rank >= obj.rank:
                        object.rank += 1
                        object.save()
        return super().save_model(request, obj, form, change)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('title', 'rank')
    list_editable = ('rank',)
    ordering = ('rank',)

    def save_model(self, request, obj, form, change):
        objects = Social.objects.all()
        for object in objects:
            if object.rank >= obj.rank and not change:
                object.rank = object.rank + 1
                object.save()
        if change:
            obj_count_before = Social.objects.get(id=obj.id)
            for object in objects:
                if object.rank > obj_count_before.rank:
                    object.rank -= 1
                    object.save()
                    if object.rank >= obj.rank:
                        object.rank += 1
                        object.save()
        return super().save_model(request, obj, form, change)
