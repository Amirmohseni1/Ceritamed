from django.conf.urls import handler500 , handler404
from django.contrib import admin
from django.urls import path, include

from .sitemap import StaticSitemap, PostsList, ServiceCategoryList, \
    ServiceList, BlogCategoryList, DoctorList
from .views import home_page
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views


# -------------sitemap-------------
sitemaps = {
    "StaticSitemap": StaticSitemap,
    'BlogCategoryList': BlogCategoryList,
    'PostsList': PostsList,
    'ServiceCategoryList': ServiceCategoryList,
    'ServiceList': ServiceList,
    'DoctorList': DoctorList
}

# -------------static setting-------------
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_page, name="Home"),
    path('', include("about_us.urls"), ),
    path('', include("services.urls"), name='services_list'),
    path('', include("contact.urls"), ),
    path('', include("doctors.urls")),
    path('', include("blog.urls")),
    path('ckeditor', include("ckeditor_uploader.urls")),
    path('admin/', admin.site.urls),
    path('sitemap.xml', views.index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]


admin.site.site_header = 'Core'
admin.site.site_title = 'Core'

if settings.DEBUG:
    # debug_toolbar
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    # static file
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
