from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from doctors.models import DoctorExpertise
from libs.db.models import SeoModel, StatusModel, AuditableModel
from .managers import ArticleManager, ArticleCategoryManager


class Article(AuditableModel, StatusModel, SeoModel):
    img = models.ImageField(verbose_name=_('Image'), upload_to='articles', null=True, blank=True)
    tag = models.ManyToManyField(verbose_name=_('tags'), to='ArticleTag', db_index=True)
    body = RichTextUploadingField(verbose_name=_('Body'))
    category = models.ManyToManyField(verbose_name=_('category'), to='ArticleCategory', db_index=True, related_name='Categories')
    doctor = models.ForeignKey(DoctorExpertise, verbose_name="پزشک های مرتبط", on_delete=models.CASCADE, null=True, blank=True, related_name='Doctor_Expertiseee')
    visit = models.IntegerField(verbose_name=_('Visits'), editable=False, default=0)

    # Article images different size
    img_thumbnail_Big = ImageSpecField(source='img', processors=[ResizeToFill(700, 400)], format='WEBP', options={'quality': 80})
    img_thumbnail_medium = ImageSpecField(source='img', processors=[ResizeToFill(350, 200)], format='WEBP', options={'quality': 80})
    img_thumbnail_small = ImageSpecField(source='img', processors=[ResizeToFill(80, 80)], format='WEBP', options={'quality': 90})

    objects = models.Manager()
    custom_objects = ArticleManager()

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def get_absolute_url(self):
        return reverse('Article:Detail', args=[self.slug])

    def admin_thumbnail(self):
        return format_html(
            "<img width=100 style='border-radius: 8px; ' src='{}'>".format(self.img_thumbnail_medium.url))


class ArticleCategory(AuditableModel, StatusModel, SeoModel):
    objects = models.Manager()
    custom_objects = ArticleCategoryManager()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class ArticleTag(AuditableModel, StatusModel, SeoModel):
    class Meta:
        verbose_name_plural = _('Tag')
        verbose_name = _('Tags')


class ArticleComment(AuditableModel, StatusModel, SeoModel):
    article = models.ForeignKey(verbose_name=_('Article'), db_index=True, to=Article, related_name='Articles',
                                on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('User name'), max_length=150)
    email = models.EmailField(verbose_name=_('Email'))
    body = models.TextField(verbose_name=_('Body'))

    class Meta:
        verbose_name_plural = _('Comment')
        verbose_name = _('Comments')
