import os
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# --------------------------------------------------- User avatar rename --------------------------------------------------------


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path_avatar(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"makeup-user-{instance.id}{ext}"
    return f"User_Avatars/{final_name}"


# --------------------------------------------------- customize User model --------------------------------------------------------

class User(AbstractUser):
    user_gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    avatar = models.ImageField(upload_to=upload_image_path_avatar, null=True, blank=True, verbose_name='Avatar')
    website = models.CharField(max_length=100, null=True, blank=True, verbose_name='Website')
    is_ban = models.BooleanField(verbose_name='block yes / no ', default=False)
    phone = models.CharField(verbose_name='Phone Number', max_length=20, null=True, blank=True)
    address = models.TextField(verbose_name='Address', null=True, blank=True)

    objects = UserManager()
