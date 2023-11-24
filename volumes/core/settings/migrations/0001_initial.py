# Generated by Django 4.2.7 on 2023-11-24 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Website name')),
                ('logo', models.ImageField(upload_to='setting/logo', verbose_name='Logo')),
                ('number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone number 1')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Setting',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Active / Deactivate')),
                ('is_deleted', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Delete / Not Delete')),
                ('image', models.ImageField(null=True, upload_to='setting/slider', verbose_name='Slider')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('body', models.TextField(verbose_name='body')),
                ('changed_active_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='active%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('changed_deleted_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
        migrations.CreateModel(
            name='PartnerCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Active / Deactivate')),
                ('is_deleted', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Delete / Not Delete')),
                ('image', models.FileField(null=True, upload_to='setting/partner-company', verbose_name='Image')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('changed_active_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='active%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('changed_deleted_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'Partner Company',
                'verbose_name_plural': 'Partner Companies',
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Active / Deactivate')),
                ('is_deleted', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Delete / Not Delete')),
                ('disease', models.CharField(max_length=50, verbose_name='disease')),
                ('image', models.ImageField(null=True, upload_to='setting/customers', verbose_name='Image')),
                ('body', models.TextField(verbose_name='Body')),
                ('changed_active_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='active%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('changed_deleted_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deleted%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'FeedBack',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
    ]
