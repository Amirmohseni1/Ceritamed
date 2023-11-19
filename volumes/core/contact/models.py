from django.db import models
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField

from utils.Base.BaseModel import BaseModel
from utils.Services.MailService import EmailService


class ContactUsForm(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=150, verbose_name='ایمیل')
    subject = models.CharField(max_length=300, verbose_name='موضوع')
    date = models.DateTimeField(auto_now=True, verbose_name='تاریخ ارسال')
    text = models.TextField(verbose_name='متن پیام')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده / خوانده نشده')
    is_result = models.TextField(verbose_name='نتیجه پیگیری', blank=True, null=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس با ما"
        ordering = ['-date']


class Form(BaseModel):
    GENDER_CHOICES = [
        ('m', 'مرد'),
        ('f', 'زن'),
    ]
    full_name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی', null=True, blank=True)
    phone = PhoneNumberField(null=False, blank=False, verbose_name='شماره تلفن')
    email = models.EmailField(max_length=150, verbose_name='ایمیل', null=True, blank=True)
    text = models.TextField(verbose_name='متن پیام', null=True, blank=True)
    where = models.URLField(verbose_name='صفحه ارسال فرم', max_length=300, null=True, blank=True)
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده / خوانده نشده')
    is_result = models.TextField(verbose_name='نتیجه پیگیری', blank=True, null=True)
    age = models.PositiveIntegerField(default=0, verbose_name='سن', blank=True, null=True)
    gender = models.CharField(max_length=1, verbose_name='جنس', choices=GENDER_CHOICES, blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name='کشور', blank=True, null=True)
    sickness = models.CharField(max_length=100, verbose_name='بیماری', blank=True, null=True)
    absorption_channel = models.CharField(max_length=100, verbose_name='کانال جذب', blank=True, null=True)
    description = models.CharField(max_length=100, verbose_name='توضیحات', blank=True, null=True)
    follow_up_1 = models.BooleanField(default=False, verbose_name='دو روز بعد')
    follow_up_2 = models.BooleanField(default=False, verbose_name='دو هفته بعد')
    follow_up_3 = models.BooleanField(default=False, verbose_name='یک ماه بعد')
    follow_up_4 = models.BooleanField(default=False, verbose_name='یک سال بعد')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "فرم"
        verbose_name_plural = "فرم ها"
        ordering = ['-created_date']


def send_email(sender, instance, created, **kwargs):
    if created:
        EmailService.send_email(
            subject=f'فرم از طرف : {instance.full_name}',
            context={'form': instance},
            template_address='Emails/form.html',
            to='ceritamed@gmail.com',
        )


post_save.connect(send_email, sender=Form)


class Newsletters(models.Model):
    email = models.CharField(max_length=150, verbose_name='ایمیل')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "ایمیل"
        verbose_name_plural = "ایمیل ها"
        ordering = ['-date']
