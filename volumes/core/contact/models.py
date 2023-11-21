from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from libs.utils.mail import EmailService
from libs.db.models import SeoModel, StatusModel, AuditableModel


class ContactUs(AuditableModel, StatusModel):
    email = models.EmailField(verbose_name=_('Email'))
    subject = models.CharField(verbose_name=_('Subject'), max_length=300)
    body = models.TextField(verbose_name=_('Body'))
    is_read = models.BooleanField(verbose_name=_('Is read'), default=False)

    created_by = None
    is_active = None
    changed_active_by = None

    def __str__(self):
        return f'{self.title} - {self.subject}'

    class Meta:
        verbose_name = _('Contact Us')
        verbose_name_plural = _('Contact Us')


class Consultation(AuditableModel, StatusModel):
    phone = PhoneNumberField(verbose_name=_('Phone number'), null=False, blank=False)
    body = models.TextField(verbose_name=_('Body'), null=True, blank=True)
    is_read = models.BooleanField(verbose_name=_('is Read'), default=False)
    source = models.URLField(verbose_name=_('Page source'), null=True, blank=True)

    created_by = None
    is_active = None
    changed_active_by = None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Consultation')
        verbose_name_plural = _('Consultation')


def send_email(sender, instance, created, **kwargs):
    if created:
        EmailService.send_email(
            subject=f'from : {instance.full_name}',
            context={'contact': instance},
            template_address='emails/contact.html',
            to='ceritamed@gmail.com',
        )


post_save.connect(send_email, sender=Consultation)


class Newsletters(models.Model):
    email = models.CharField(verbose_name=_('Email'), max_length=150)
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')
        ordering = ['-created_at']
