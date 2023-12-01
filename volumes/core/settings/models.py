from django.db import models
from django.utils.translation import gettext_lazy as _

from libs.db.models import AuditableModel, SeoModel, StatusModel
from .managers import SliderManger, SocialManger, PartnerCompanyManger, FeedBackManger


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
    rank = models.PositiveSmallIntegerField(verbose_name=_('Rank'), default=1)

    objects = models.Manager()
    custom_objects = SliderManger()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        objects = Slider.objects.all().count()
        if self.rank > objects:
            self.rank = objects + 1
        return super(Slider, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def delete(self, using=None, keep_parents=False):
        objects = Slider.objects.all()
        for object in objects:
            if object.rank > self.rank:
                object.rank -= 1
                object.save()
        return super(Slider, self).delete(using=None, keep_parents=False)

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural = _('Sliders')


class PartnerCompany(AuditableModel, StatusModel):
    image = models.FileField(verbose_name=_('Image'), upload_to='setting/partner-company', null=True)
    url = models.URLField(verbose_name=_('URL'), null=True, blank=True)
    rank = models.PositiveSmallIntegerField(verbose_name=_('Rank'), default=1)

    objects = models.Manager()
    custom_objects = PartnerCompanyManger()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        objects = PartnerCompany.objects.all().count()
        if self.rank > objects:
            self.rank = objects + 1
        return super(PartnerCompany, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def delete(self, using=None, keep_parents=False):
        objects = PartnerCompany.objects.all()
        for object in objects:
            if object.rank > self.rank:
                object.rank -= 1
                object.save()
        return super(PartnerCompany, self).delete(using=None, keep_parents=False)

    class Meta:
        verbose_name = _('Partner Company')
        verbose_name_plural = _('Partner Companies')


class FeedBack(AuditableModel, StatusModel):
    disease = models.CharField(verbose_name=_('disease'), max_length=50)
    image = models.ImageField(verbose_name=_('Image'), upload_to='setting/customers', null=True)
    body = models.TextField(verbose_name=_('Body'))
    rank = models.PositiveSmallIntegerField(verbose_name=_('Rank'), default=1)

    objects = models.Manager()
    custom_objects = FeedBackManger()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        objects = FeedBack.objects.all().count()
        if self.rank > objects:
            self.rank = objects + 1
        return super(FeedBack, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def delete(self, using=None, keep_parents=False):
        objects = FeedBack.objects.all()
        for object in objects:
            if object.rank > self.rank:
                object.rank -= 1
                object.save()
        return super(FeedBack, self).delete(using=None, keep_parents=False)

    class Meta:
        verbose_name = _('FeedBack')
        verbose_name_plural = _('Feedbacks')


class Social(AuditableModel, StatusModel):
    url = models.URLField(verbose_name=_('Link'))
    icon = models.CharField(verbose_name=_('Icon'), max_length=20)
    rank = models.PositiveSmallIntegerField(verbose_name=_('Rank'), default=1)

    objects = models.Manager()
    custom_objects = SocialManger()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        objects = Social.objects.all().count()
        if self.rank > objects:
            self.rank = objects + 1
        return super(Social, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def delete(self, using=None, keep_parents=False):
        objects = Social.objects.all()
        for object in objects:
            if object.rank > self.rank:
                object.rank -= 1
                object.save()
        return super(Social, self).delete(using=None, keep_parents=False)

    class Meta:
        verbose_name = _('Social')
        verbose_name_plural = _('Socials')
