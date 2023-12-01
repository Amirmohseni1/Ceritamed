from django.db import models


class SliderManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, is_deleted=False).order_by('-order')


class PartnerCompanyManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, is_deleted=False).order_by('-order')


class FeedBackManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, is_deleted=False).order_by('-order')


class SocialManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, is_deleted=False)
