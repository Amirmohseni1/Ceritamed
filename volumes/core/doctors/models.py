import os
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.urls import reverse


class DoctorEvidence(models.Model):
    skills_evidence = models.CharField(max_length=50, verbose_name="سطح تحصیلی")
    skills_expertise_slug = models.SlugField(unique=True, verbose_name="url سطح تحصیلی", null=True)

    def __str__(self):
        return self.skills_evidence

    class Meta:
        verbose_name = " سطح تحصیل"
        verbose_name_plural = "سطح تحصیلی"


class DoctorExpertise(models.Model):
    skills_expertise = models.CharField(max_length=50, verbose_name="عنوان تخصص پزشک")
    skills_expertise_slug = models.SlugField(unique=True, verbose_name="url تخصص پزشک", null=True)

    def __str__(self):
        return self.skills_expertise

    class Meta:
        verbose_name = "تخصص پزشک"
        verbose_name_plural = " تخصص پزشکان"


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Ceritamed-Doctor {instance.slug}{ext}"
    return f"Doctor/{final_name}"


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100, verbose_name="اسم دکتر")
    slug = models.SlugField(unique=True, verbose_name="URL (به انگلیسی)", null=True)
    doctor_img = models.ImageField(upload_to=upload_image_path, null=True, verbose_name="عکس پزشک", help_text='ابعاد مناسب عکس پزشکان 385 * 385 px')
    img_thumbnail_big = ImageSpecField(source='doctor_img',
                                       processors=[ResizeToFill(385, 385)],
                                       format='JPEG',
                                       options={'quality': 90})
    img_thumbnail_medium = ImageSpecField(source='doctor_img',
                                          processors=[ResizeToFill(205, 205)],
                                          format='JPEG',
                                          options={'quality': 90})
    img_thumbnail_small = ImageSpecField(source='doctor_img',
                                         processors=[ResizeToFill(102, 102)],
                                         format='JPEG',
                                         options={'quality': 1000})
    about_doctor = models.TextField(verbose_name="درباره دکتر")
    doctor_expertise = models.ForeignKey(DoctorExpertise, verbose_name="تخصص پزشک", on_delete=models.CASCADE, null=True)
    doctor_evidence = models.ForeignKey(DoctorEvidence, verbose_name="سطح تحصیلی", on_delete=models.CASCADE, null=True)
    doctor_skill_description = models.TextField(verbose_name="توضیح کوتاه مهارت ها")
    doctor_education_description = models.TextField(verbose_name="توضیح کوتاه تحصیلات", null=True)
    doctor_experience_years = models.IntegerField(verbose_name="تجربه کاری", null=True)
    doctor_education_place = models.CharField(max_length=150, verbose_name="محل تحصیل", null=True, )
    active = models.BooleanField(default=False, verbose_name="فعال / یا غیره فعال")
    home_page = models.BooleanField(default=False, verbose_name="صفحه اصلی")

    def __str__(self):
        return self.doctor_name

    def get_absolute_url(self):
        return reverse('Doctor:Detail', args=[self.slug])

    class Meta:
        verbose_name = "پزشک"
        verbose_name_plural = "پزشکان"
