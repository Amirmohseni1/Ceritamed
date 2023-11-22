from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from libs.db.models import SeoModel, StatusModel, AuditableModel


class Service(AuditableModel, SeoModel, StatusModel):
    img = models.ImageField(verbose_name=_('Image'), upload_to='services', null=True)
    icon = models.ImageField(verbose_name=_('Icon'), upload_to='service/icon', null=True, max_length=15)
    price = models.PositiveSmallIntegerField(verbose_name=_('Price'), default=0, null=True, blank=True)
    body = RichTextUploadingField(verbose_name=_('Body'), null=True)
    category = models.ManyToManyField(verbose_name=_('Category'), to='ServiceCategory', blank=True, related_name='categories')
    index = models.BooleanField(verbose_name=_('Show in index page'), default=False)

    def get_absolute_url(self):
        return reverse('Service:Details', args=[self.pk, self.slug])

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')


class ServiceCategory(AuditableModel, StatusModel, SeoModel):
    icon = models.ImageField(verbose_name=_('Icon'), upload_to='service-category/icon')
    img = models.ImageField(verbose_name=_('Image'), upload_to='service-category', null=True)
    index = models.BooleanField(verbose_name=_('Show in index page'), default=False)

    def get_absolute_url(self):
        return reverse('Service:Categories', args=[self.slug])

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
