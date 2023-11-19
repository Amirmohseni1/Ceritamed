import os
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Ceritamed-Slider-{instance.title}{ext}"
    return f"ُSlider/{final_name}"


class Slider(models.Model):
    title = models.CharField(max_length=65, verbose_name="عنوان")
    category = models.CharField(max_length=65, verbose_name="دسته بندی", null=True)
    img = models.ImageField(upload_to=upload_image_path, null=True, verbose_name="عکس پس زمینه")
    btn = models.CharField(max_length=50, default='کلیک کنید', help_text='متن پیش فرض ( کلیک کنید ) هستش', blank=True, null=True)
    link = models.URLField(max_length=200, verbose_name="لینک", blank=True, null=True)
    slider_img = ImageSpecField(source='img', processors=[ResizeToFill(1440, 744)], format='JPEG', options={'quality': 80})
    descriptions = models.TextField(verbose_name="محتوا")
    active = models.BooleanField(default=False, verbose_name='فعال / غیره فعال')

    class Meta:
        verbose_name = "اسلادر"
        verbose_name_plural = "اسلایدر ها"

    def __str__(self):
        return self.title


# --------------------------------------------------- partners img rename --------------------------------------------------------

def upload_image_path_partners(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Ceritamed-partners-{instance.title}{ext}"
    return f"partners-logo/{final_name}"


# --------------------------------------------------- partners --------------------------------------------------------

class Partners(models.Model):
    title = models.CharField(max_length=150, verbose_name="نام شرکت")
    img = models.FileField(upload_to=upload_image_path_partners, null=True, verbose_name="عکس لوگو",
                           help_text='ابعاد عکس 164 * 82')
    url = models.URLField(null=True, blank=True, verbose_name="لینک")
    active = models.BooleanField(default=False, verbose_name='فعال / غیره فعال')

    class Meta:
        verbose_name = "پارتنر"
        verbose_name_plural = "پارتنر ها"

    def __str__(self):
        return self.title

    img_thumbnail = ImageSpecField(source='img',
                                   processors=[ResizeToFill(184, 90)],
                                   format='PNG',
                                   options={'quality': 100})


# --------------------------------------------------- partners img rename --------------------------------------------------------

def upload_image_path_customers(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Ceritamed-customers-{instance.name}{ext}"
    return f"customers-img/{final_name}"


# --------------------------------------------------- customers --------------------------------------------------------

class Customers(models.Model):
    name = models.CharField(max_length=150, verbose_name="نام مشتری")
    problem = models.CharField(max_length=50, verbose_name='بیماری درمان شده')
    img = models.ImageField(upload_to=upload_image_path_customers, null=True, verbose_name="عکس مشتری",
                            help_text='ابعاد عکس 85 * 85 px')
    customers_img = ImageSpecField(source='img',
                                   processors=[ResizeToFill(85, 85)],
                                   format='JPEG',
                                   options={'quality': 70})
    text = models.TextField(verbose_name='نظره مشتری')
    active = models.BooleanField(default=False, verbose_name='فعال / غیره فعال')

    class Meta:
        verbose_name = "نظر مشتری"
        verbose_name_plural = "نظر مشتری ها"

    def __str__(self):
        return self.name


# --------------------------------------------------- Home page Data --------------------------------------------------------

class HomeData(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    img = models.FileField(upload_to="Home_data_icons", null=True, verbose_name="ایکون",
                           help_text='ابعاد عکس 45 * 45 px و کده رنگ #19ce67')
    number = models.IntegerField(verbose_name='تعداد')
    active = models.BooleanField(default=False, verbose_name='فعال / غیره فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "امار سایت"
        verbose_name_plural = "امار های سایت"
