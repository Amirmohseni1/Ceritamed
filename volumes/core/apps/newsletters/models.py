from django.db import models

# Create your models here.
class Newsletters(models.Model):
    email = models.CharField(max_length=150, verbose_name='ایمیل')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "ایمیل"
        verbose_name_plural = "ایمیل ها"
        ordering = ['-date']
