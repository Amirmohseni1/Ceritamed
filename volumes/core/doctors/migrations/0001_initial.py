# Generated by Django 3.1 on 2023-11-21 19:36

from django.db import migrations, models
import django.db.models.deletion
import doctors.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorEvidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills_evidence', models.CharField(max_length=50, verbose_name='سطح تحصیلی')),
                ('skills_expertise_slug', models.SlugField(null=True, unique=True, verbose_name='url سطح تحصیلی')),
            ],
            options={
                'verbose_name': ' سطح تحصیل',
                'verbose_name_plural': 'سطح تحصیلی',
            },
        ),
        migrations.CreateModel(
            name='DoctorExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills_expertise', models.CharField(max_length=50, verbose_name='عنوان تخصص پزشک')),
                ('skills_expertise_slug', models.SlugField(null=True, unique=True, verbose_name='url تخصص پزشک')),
            ],
            options={
                'verbose_name': 'تخصص پزشک',
                'verbose_name_plural': ' تخصص پزشکان',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100, verbose_name='اسم دکتر')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='URL (به انگلیسی)')),
                ('doctor_img', models.ImageField(help_text='ابعاد مناسب عکس پزشکان 385 * 385 px', null=True, upload_to=doctors.models.upload_image_path, verbose_name='عکس پزشک')),
                ('about_doctor', models.TextField(verbose_name='درباره دکتر')),
                ('doctor_skill_description', models.TextField(verbose_name='توضیح کوتاه مهارت ها')),
                ('doctor_education_description', models.TextField(null=True, verbose_name='توضیح کوتاه تحصیلات')),
                ('doctor_experience_years', models.IntegerField(null=True, verbose_name='تجربه کاری')),
                ('doctor_education_place', models.CharField(max_length=150, null=True, verbose_name='محل تحصیل')),
                ('active', models.BooleanField(default=False, verbose_name='فعال / یا غیره فعال')),
                ('home_page', models.BooleanField(default=False, verbose_name='صفحه اصلی')),
                ('doctor_evidence', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctorevidence', verbose_name='سطح تحصیلی')),
                ('doctor_expertise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctorexpertise', verbose_name='تخصص پزشک')),
            ],
            options={
                'verbose_name': 'پزشک',
                'verbose_name_plural': 'پزشکان',
            },
        ),
    ]
