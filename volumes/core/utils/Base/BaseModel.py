from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    update_date = models.DateTimeField(auto_now=True, verbose_name='اخرین به روزرسانی')

    class Meta:
        abstract = True
