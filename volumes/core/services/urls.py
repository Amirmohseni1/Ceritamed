from django.urls import path
from .views import ServicesCategory, services_list, services_detail

urlpatterns = [
    path('services', ServicesCategory.as_view(), name="Services_Category"),
    path('services/<slug:slug>', services_list, name="Services_List"),
    path('services/<pk>/<slug:slug>', services_detail, name="services_detail"),
]