from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import SliderManger, SocialManger, PartnerCompanyManger, FeedBackManger
from libs.db.models import AuditableModel, SeoModel, StatusModel


class Setting(models.Model):
    title = models.CharField(verbose_name=_('Website name'), max_length=20)
    light_logo = models.ImageField(verbose_name=_('Light logo'), upload_to="setting/logo", null=True)
    dark_logo = models.ImageField(verbose_name=_('Dark logo'), upload_to="setting/logo", null=True)
    number = models.CharField(verbose_name=_('Phone number 1'), max_length=20, blank=True, null=True)
    address = models.CharField(verbose_name=_('Address'), max_length=128, blank=True, null=True)
    email = models.EmailField(verbose_name=_('Email'), null=True, blank=True)
    short_about = models.TextField(verbose_name=_('Short about'), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Setting')
        verbose_name_plural = _('Setting')


class Slider(AuditableModel, StatusModel):
    image = models.ImageField(verbose_name=_('Slider'), upload_to='setting/slider', null=True)
    url = models.URLField(verbose_name=_('Link'), blank=True, null=True)
    body = models.TextField(verbose_name=_('Body'))
    order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=0)

    objects = models.Manager()
    custom_objects = SliderManger()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        sliders = Slider.objects.all()
        for slider in sliders:
            if slider.order >= self.order:
                slider.order += 1
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def delete(self, using=None, keep_parents=False):
        sliders = Slider.objects.all()
        for slider in sliders:
            if slider.order >= self.order:
                slider.order -= 1
        return super().delete(using=None, keep_parents=False)

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural = _('Sliders')


class PartnerCompany(AuditableModel, StatusModel):
    image = models.FileField(verbose_name=_('Image'), upload_to='setting/partner-company', null=True)
    url = models.URLField(verbose_name=_('URL'), null=True, blank=True)
    order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=0)

    objects = models.Manager()
    custom_objects = PartnerCompanyManger()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        partners = PartnerCompany.objects.all()
        for partner in partners:
            if partner.order >= self.order:
                partner.order += 1
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def delete(self, using=None, keep_parents=False):
        partners = Slider.objects.all()
        for partner in partners:
            if partner.order >= self.order:
                partner.order -= 1
        return super().delete(using=None, keep_parents=False)

    class Meta:
        verbose_name = _('Partner Company')
        verbose_name_plural = _('Partner Companies')


class FeedBack(AuditableModel, StatusModel):
    disease = models.CharField(verbose_name=_('disease'), max_length=50)
    image = models.ImageField(verbose_name=_('Image'), upload_to='setting/customers', null=True)
    body = models.TextField(verbose_name=_('Body'))
    order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=0)

    objects = models.Manager()
    custom_objects = FeedBackManger()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        feeds = FeedBack.objects.all()
        for feed in feeds:
            if feed.order >= self.order:
                feed.order += 1
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def delete(self, using=None, keep_parents=False):
        feeds = Slider.objects.all()
        for feed in feeds:
            if feed.order >= self.order:
                feed.order -= 1
        return super().delete(using=None, keep_parents=False)

    class Meta:
        verbose_name = _('FeedBack')
        verbose_name_plural = _('Feedbacks')


class Social(AuditableModel, StatusModel):
    url = models.URLField(verbose_name=_('Link'))
    icon = models.CharField(verbose_name=_('Icon'), max_length=20)

    objects = models.Manager()
    custom_objects = SocialManger()

    class Meta:
        verbose_name = _('Social')
        verbose_name_plural = _('Socials')
