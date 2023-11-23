from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from libs.db.models import SeoModel, StatusModel, AuditableModel


class Doctor(AuditableModel, StatusModel, SeoModel):
    image = models.ImageField(verbose_name=_('Image'), upload_to='Doctor', null=True, blank=True)
    about = models.TextField(verbose_name='About doctor', blank=True)
    expertise = models.ForeignKey(verbose_name=_('Expertise'), to='DoctorExpertise', on_delete=models.CASCADE, null=True, blank=True)
    education = models.ForeignKey(verbose_name=_('Education'), to='DoctorEducation', on_delete=models.CASCADE, null=True, blank=True)
    experience = models.PositiveSmallIntegerField(verbose_name="Experience year", null=True, blank=True)
    index = models.BooleanField(default=False, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('Doctor:Detail', args=[self.slug])

    class Meta:
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctors')


class DoctorEducation(AuditableModel, StatusModel):
    class Meta:
        verbose_name = _('Education')
        verbose_name_plural = _('Educations')


class DoctorExpertise(AuditableModel, StatusModel):


    class Meta:
        verbose_name = _('Expertise')
        verbose_name_plural = _('Expertise')
