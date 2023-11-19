# Generated by Django 3.1 on 2023-11-19 06:48

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='doctors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Doctor_Expertiseee', to='doctors.doctorexpertise', verbose_name='پزشک های مرتبط'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='تگ ها و کلمات کلیدی'),
        ),
    ]
