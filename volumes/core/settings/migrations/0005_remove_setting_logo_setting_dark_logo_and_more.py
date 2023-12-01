# Generated by Django 4.2.7 on 2023-12-01 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_alter_setting_address_alter_setting_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='logo',
        ),
        migrations.AddField(
            model_name='setting',
            name='dark_logo',
            field=models.ImageField(null=True, upload_to='setting/logo', verbose_name='Logo'),
        ),
        migrations.AddField(
            model_name='setting',
            name='light_logo',
            field=models.ImageField(null=True, upload_to='setting/logo', verbose_name='Logo'),
        ),
    ]
