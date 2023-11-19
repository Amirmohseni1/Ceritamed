import os
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils import timezone


# -------------------------------------------------- Servise object  --------------------------------------------------------

class ServiceObject(models.Manager):
    # -------------------- Servise object active ------------------

    def active_Servise(self):
        return self.get_queryset().filter(active=True)


# --------------------------------------------------- Servise_category img rename --------------------------------------------------------


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Ceritamed-{instance.title}{ext}"
    return f"Servise_category/{final_name}"


# --------------------------------------------------- Servise icons rename --------------------------------------------------------


def upload_image_path_servise_icons(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Ceritamed-{instance.title}{ext}"
    return f"icon/{final_name}"


# --------------------------------------------------- Servise_category DB --------------------------------------------------------

class ServiceCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان خدمت')
    png_img = models.FileField(upload_to=upload_image_path_servise_icons, null=True, verbose_name='ایکون',
                               help_text='ابعاد مناسب 30 * 30 px')
    png_img_home = models.FileField(upload_to=upload_image_path_servise_icons, null=True,
                                    verbose_name='ایکون صفحه اصلی', help_text='ابعاد مناسب 35 * 35 px')
    img = models.ImageField(upload_to=upload_image_path, null=True, verbose_name='عکس')
    img_thumbnail = ImageSpecField(source='img',
                                   processors=[ResizeToFill(350, 360)],
                                   format='JPEG',
                                   options={'quality': 60})
    descriptions = models.TextField(max_length=200, null=True, verbose_name='توضیح کوتاه')
    slug = models.SlugField(unique=True, verbose_name='url صفحه')
    active = models.BooleanField(default=False, verbose_name='فعال / غیره فعال')
    active_home = models.BooleanField(default=False, verbose_name='صفحه اول سایت')

    def get_absolute_url(self):
        return f"/services/{self.slug.replace(' ', '-')}"

    class Meta:
        verbose_name = "دستته خدمت"
        verbose_name_plural = "دسته خدمت ها"

    def __str__(self):
        return self.title


# --------------------------------------------------- Servise img rename --------------------------------------------------------


def upload_image_path_Servise(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Ceritamed-{instance.title}{ext}"
    return f"Servise/{final_name}"


# --------------------------------------------------- Servise DB --------------------------------------------------------


class Service(models.Model):
    seo = models.CharField(max_length=150, verbose_name='عنوان Seo', help_text='این عنوان داخل تگ title قرار میگیره', null=True)
    title = models.CharField(max_length=150, verbose_name='عنوان خدمت',
                             help_text='این عنوان اصلی خدمت هستش ( پروتز دنداد و امپلنت ...)')
    h1 = models.CharField(max_length=65, verbose_name=" تگ H1", null=True)
    img = models.ImageField(upload_to=upload_image_path_Servise, null=True, verbose_name='عکس')
    png_img = models.FileField(upload_to=upload_image_path_servise_icons, null=True, verbose_name='ایکون')
    slug = models.SlugField(unique=True, null=True, verbose_name='URL خدمت')
    price = models.IntegerField(verbose_name='قیمت خدمت', default=0, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, verbose_name='متا دیسکریپشن')
    descriptions = RichTextUploadingField(verbose_name="محتوا", null=True,
                                          external_plugin_resources=
                                          [('youtube', '/static/ckeditor/ckeditor/plugins/youtube/youtube/',
                                            'plugin.js'), ])
    img_thumbnail_Big = ImageSpecField(source='img',
                                       processors=[ResizeToFill(1500, 700)],
                                       format='JPEG',
                                       options={'quality': 70})
    img_thumbnail_medium = ImageSpecField(source='img',
                                          processors=[ResizeToFill(350, 360)],
                                          format='JPEG',
                                          options={'quality': 60})
    s_category = models.ManyToManyField(ServiceCategory, blank=True, verbose_name="دسته بندی خدمات",
                                        related_name='Servise_category')
    publish = models.DateTimeField(default=timezone.now, null=True, verbose_name="تاریخ انتشار")
    active = models.BooleanField(default=False, verbose_name='فعال / غیره فعال')
    active_home = models.BooleanField(default=False, verbose_name='صفحه اول سایت')

    def get_absolute_url(self):
        return f"/services/{self.pk}/{self.slug.replace(' ', '-')}"

    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = "خدمت ها"

    def __str__(self):
        return self.title

    object = ServiceObject()
    

class ServicePrice(models.Model):
    service = models.ForeignKey(Service, verbose_name='خدمت', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='اسم کشور')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت به دلار')

    class Meta:
        verbose_name = "تفاوت قیمت"
        verbose_name_plural = "تفاوت قیمت"

    def __str__(self):
        return self.name

