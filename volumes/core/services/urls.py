from django.urls import path
from .views import ServicesCategory, services_list, services_detail

app_name = 'Service'
urlpatterns = [
    path('', ServicesCategory.as_view(), name="Categories"),
    path('<slug:slug>/', services_list, name="Category-Childes"),
    path('<pk>/<slug:slug>/', services_detail, name="Details"),
]