from django.urls import path
from .views import DoctorsListView ,doctors_detail


urlpatterns = [
    path('doctors', DoctorsListView.as_view(), name="Doctors_list"),
    path('doctors/<slug:slug>', doctors_detail, name="Doctors_Detail"),
]