from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class AuditableModel(models.Model):
    title = models.CharField(verbose_name=_('Title'), db_index=True, max_length=255)
    created_by = models.ForeignKey(verbose_name=_('Created by'), editable=False, to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                   related_name="created%(app_label)s_%(class)s_related")
    created_at = models.DateTimeField(verbose_name=_('Created at'), editable=False, auto_now_add=True, blank=True, null=True)
    modified_by = models.ForeignKey(verbose_name=_('Modified by'), editable=False, to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                    related_name="updated%(app_label)s_%(class)s_related")
    modified_at = models.DateTimeField(verbose_name=_('Modified at'), editable=False, auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ['-created_at']


class StatusModel(models.Model):
    changed_active_by = models.ForeignKey(verbose_name=_('Created by'), editable=False, to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                          related_name="active%(app_label)s_%(class)s_related")
    is_active = models.BooleanField(verbose_name=_('Active / Deactivate'), default=False, db_index=True, blank=True, null=True)
    changed_deleted_by = models.ForeignKey(verbose_name=_('Modified by'), editable=False, to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                           related_name="deleted%(app_label)s_%(class)s_related")
    is_deleted = models.BooleanField(verbose_name=_('Delete / Not Delete'), default=False, db_index=True, blank=True, null=True)

    class Meta:
        abstract = True


class SeoModel(models.Model):
    slug = models.SlugField(verbose_name=_('Slug (URl)'), db_index=True, unique=True, allow_unicode=True, null=True)
    meta_description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    meta_canonical = models.URLField(verbose_name=_('Canonical'), blank=True, null=True)

    class Meta:
        abstract = True