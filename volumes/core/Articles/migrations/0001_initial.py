# Generated by Django 3.1 on 2023-11-21 19:36

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Active / Deactivate')),
                ('is_deleted', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Delete / Not Delete')),
                ('slug', models.SlugField(allow_unicode=True, null=True, unique=True, verbose_name='Slug (URl)')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('meta_canonical', models.URLField(blank=True, null=True, verbose_name='Canonical')),
                ('img', models.ImageField(blank=True, null=True, upload_to='articles', verbose_name='Image')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Body')),
                ('visit', models.IntegerField(default=0, editable=False, verbose_name='Visits')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Active / Deactivate')),
                ('is_deleted', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Delete / Not Delete')),
                ('slug', models.SlugField(allow_unicode=True, null=True, unique=True, verbose_name='Slug (URl)')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('meta_canonical', models.URLField(blank=True, null=True, verbose_name='Canonical')),
                ('changed_active_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activearticles_articletag_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('changed_deleted_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deletedarticles_articletag_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='createdarticles_articletag_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updatedarticles_articletag_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'Tags',
                'verbose_name_plural': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Active / Deactivate')),
                ('is_deleted', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Delete / Not Delete')),
                ('slug', models.SlugField(allow_unicode=True, null=True, unique=True, verbose_name='Slug (URl)')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('meta_canonical', models.URLField(blank=True, null=True, verbose_name='Canonical')),
                ('name', models.CharField(max_length=150, verbose_name='User name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('body', models.TextField(verbose_name='Body')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Articles', to='Articles.article', verbose_name='Article')),
                ('changed_active_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activearticles_articlecomment_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('changed_deleted_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deletedarticles_articlecomment_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='createdarticles_articlecomment_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updatedarticles_articlecomment_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'Comments',
                'verbose_name_plural': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modified at')),
                ('is_active', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Active / Deactivate')),
                ('is_deleted', models.BooleanField(blank=True, db_index=True, default=False, null=True, verbose_name='Delete / Not Delete')),
                ('slug', models.SlugField(allow_unicode=True, null=True, unique=True, verbose_name='Slug (URl)')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('meta_canonical', models.URLField(blank=True, null=True, verbose_name='Canonical')),
                ('changed_active_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activearticles_articlecategory_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('changed_deleted_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deletedarticles_articlecategory_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='createdarticles_articlecategory_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updatedarticles_articlecategory_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(db_index=True, related_name='Categories', to='Articles.ArticleCategory', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='article',
            name='changed_active_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activearticles_article_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='article',
            name='changed_deleted_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deletedarticles_article_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AddField(
            model_name='article',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='createdarticles_article_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='article',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Doctor_Expertiseee', to='doctors.doctorexpertise', verbose_name='پزشک های مرتبط'),
        ),
        migrations.AddField(
            model_name='article',
            name='modified_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updatedarticles_article_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(db_index=True, to='Articles.ArticleTag', verbose_name='tags'),
        ),
    ]
