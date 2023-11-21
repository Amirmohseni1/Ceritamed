from django.contrib import admin
from django.contrib.sitemaps import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .sitemap import StaticSitemap, PostsList, ServiceCategoryList, \
    ServiceList, BlogCategoryList, DoctorList

sitemaps = {
    "StaticSitemap": StaticSitemap,
    'BlogCategoryList': BlogCategoryList,
    'PostsList': PostsList,
    'ServiceCategoryList': ServiceCategoryList,
    'ServiceList': ServiceList,
    'DoctorList': DoctorList
}
sitemap = [
    path('sitemap.xml', views.index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]


urlpatterns = [
    path('', include('home.urls', namespace='Home')),
    path('article/', include("Articles.urls", namespace='Article')),
    path('service/', include("services.urls"), name='Service'),
    path('doctor/', include("doctors.urls"), name='Doctor'),
    path('ckeditor', include("ckeditor_uploader.urls")),
    path('admin/', admin.site.urls),
] + sitemap

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
