# Generated by Django 4.2.7 on 2023-12-01 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_feedback_order_partnercompany_order_setting_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='address',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone number 1'),
        ),
    ]
