from django.db import models
from django.utils.translation import gettext_lazy as _

from libs.db.models import AuditableModel, SeoModel, StatusModel


class Setting(models.Model):
    title = models.CharField(verbose_name=_('Website name'), max_length=20)
    logo = models.ImageField(verbose_name=_('Logo'), upload_to="setting/logo")
    number = models.CharField(verbose_name=_('Phone number 1'), max_length=15, blank=True, null=True)
    address = models.TextField(verbose_name=_('Address'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Setting')
        verbose_name_plural = _('Setting')


class Slider(AuditableModel, StatusModel):
    image = models.ImageField(verbose_name=_('Slider'), upload_to='setting/slider', null=True)
    url = models.URLField(verbose_name=_('URL'), blank=True, null=True)
    body = models.TextField(verbose_name=_('body'))

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural = _('Sliders')


class PartnerCompany(AuditableModel, StatusModel):
    image = models.FileField(verbose_name=_('Image'), upload_to='setting/partner-company', null=True)
    url = models.URLField(verbose_name=_('URL'), null=True, blank=True)

    class Meta:
        verbose_name = _('Partner Company')
        verbose_name_plural = _('Partner Companies')


class FeedBack(AuditableModel, StatusModel):
    disease = models.CharField(verbose_name=_('disease'), max_length=50)
    image = models.ImageField(verbose_name=_('Image'), upload_to='setting/customers', null=True)
    body = models.TextField(verbose_name=_('Body'))

    class Meta:
        verbose_name = _('FeedBack')
        verbose_name_plural = _('Feedbacks')
