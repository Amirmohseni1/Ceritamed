from django.urls import path
from .views import Index, AboutUs, ContactUs

app_name = 'Home'
urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('about-us/', AboutUs.as_view(), name='About-Us'),
    path('contact/', ContactUs.as_view(), name="Contact-Us"),
]
