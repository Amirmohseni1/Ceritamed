import os
from django.http import Http404
from django.db import models
from django.db.models import Q
from django.utils.html import format_html
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ..doctors.models import DoctorExpertise


# --------------------------------------------------- blog Object --------------------------------------------------------


class PostObject(models.Manager):
    # -------------------- blog object search ------------------
    def search(self, qoury):
        lookup = (
                Q(title__icontains=qoury) |
                Q(h1__icontains=qoury)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


# --------------------------------------------------- blog Category DB --------------------------------------------------------


class PostCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(unique=True, null=True, verbose_name='url')

    def get_absolute_url(self):
        return f"/blog/{self.slug.replace(' ', '-')}"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


# --------------------------------------------------- blog img rename --------------------------------------------------------


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Ceritamed-{instance.title}-{instance.created}{ext}"
    return f"blog/{final_name}"


# --------------------------------------------------- blog DB --------------------------------------------------------


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان Seo", null=True)
    h1 = models.CharField(max_length=100, verbose_name="h1", null=True)
    img = models.ImageField(upload_to=upload_image_path, verbose_name='تصویر اصلی مقاله', null=True, blank=True)
    
    img_thumbnail_Big = ImageSpecField(source='img',
                                       processors=[ResizeToFill(700, 400)],
                                       format='WEBP',
                                       options={'quality': 80})
                                       
    img_thumbnail_medium = ImageSpecField(source='img',
                                          processors=[ResizeToFill(350, 200)],
                                          format='WEBP',
                                          options={'quality': 80})
    img_thumbnail_small = ImageSpecField(source='img',
                                         processors=[ResizeToFill(80, 80)],
                                         format='WEBP',
                                         options={'quality': 90})
    tags = TaggableManager(verbose_name="تگ ها و کلمات کلیدی", )
    description = models.TextField(max_length=500, verbose_name="متا دیسکریپشن", null=True)
    slug = models.SlugField(unique=True, verbose_name=" مقاله url", null=True)
    descriptions = RichTextUploadingField(verbose_name="محتوا",
                                          null=True,
                                          external_plugin_resources=
                                          [('youtube', '/static/ckeditor/ckeditor/plugins/youtube/youtube/',
                                            'plugin.js'), ])
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار", null=True)
    publish = models.DateTimeField(default=timezone.now, null=True, verbose_name="تاریخ انتشار دستی")
    update = models.DateTimeField(auto_now=True, verbose_name="بروز رسانی", null=True)
    b_category = models.ManyToManyField(PostCategory, verbose_name="دسته بندی بلاگ", related_name='blog_category',
                                        blank=True)
    doctors = models.ForeignKey(DoctorExpertise, verbose_name="پزشک های مرتبط", on_delete=models.CASCADE, null=True,
                                blank=True, related_name='Doctor_Expertiseee')
    active = models.BooleanField(default=False, verbose_name="فعال / غیره فعال")
    blog_views = models.IntegerField(default=0, verbose_name='تعداد بازدید')

    def get_absolute_url(self):
        return f"/blog/{self.id}/{self.slug.replace(' ', '-')}"

    class Meta:
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ ها"
        ordering = ['-publish']

    def admin_thumbnail(self):
        return format_html(
            "<img width=100 style='border-radius: 8px; ' src='{}'>".format(self.img_thumbnail_medium.url))

    admin_thumbnail.short_description = "عکس"

    def get_blog_search_by_name(self):
        return f"{self.id}/{self.slug.replace(' ', '-')}"

    def __str__(self):
        return self.title

    object = PostObject()


# --------------------------------------------------- blog comment --------------------------------------------------------


class PostComment(models.Model):
    blog_post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    text = models.TextField(verbose_name='متن کامنت')
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    update = models.DateTimeField(auto_now=True, verbose_name="اپدیت")
    active = models.BooleanField(default=False, verbose_name="فال و غیر فعال")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "کامنت ها"
        verbose_name = "کامنتپ"
