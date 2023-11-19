from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from Articles.models import Article, ArticleCategory
from doctors.models import Doctor
from services.models import ServiceCategory, Service


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return ['Home', 'blog_list', 'Doctors_list', 'Services_Category', 'About-us', 'contact']

    def location(self, item):
        return reverse(item)


class BlogCategoryList(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return ArticleCategory.objects.all()


class PostsList(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Article.object.filter(active=True)


class ServiceCategoryList(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ServiceCategory.objects.filter(active=True)


class ServiceList(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Service.object.filter(active=True)


class DoctorList(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Doctor.objects.filter(active=True)
