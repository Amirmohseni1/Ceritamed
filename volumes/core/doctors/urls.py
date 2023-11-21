from django.urls import path
from .views import DoctorsListView ,doctors_detail

app_name = 'Doctor'
urlpatterns = [
    path('', DoctorsListView.as_view(), name='List'),
    path('<slug:slug>/', doctors_detail, name='Detail'),
]