from django.urls import path
from .views import home_page, about_us, contact

app_name = 'Home'
urlpatterns = [
    path('', home_page, name='Index'),
    path('about-us/', about_us, name='About-Us'),
    path('contact/', contact, name="Contact-Us"),
]
