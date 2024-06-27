# Generated by Django 5.0.6 on 2024-06-27 21:44

import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communities_Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ProfileLink', models.URLField(max_length=100)),
                ('Image', models.ImageField(upload_to=pathlib.PureWindowsPath('D:/Matrix_Backend/matrix/matrix_api/Communities_Partners_images'))),
                ('Bio', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Community_Partner',
                'verbose_name_plural': 'Communities_Partners',
            },
        ),
        migrations.CreateModel(
            name='Host_and_main_communities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('community_type', models.CharField(choices=[('H', 'Host'), ('MC', 'Main Community')], max_length=2)),
                ('ProfileLink', models.URLField(max_length=100)),
                ('Image', models.ImageField(upload_to=pathlib.PureWindowsPath('D:/Matrix_Backend/matrix/matrix_api/Host_and_main_communities_images'))),
            ],
            options={
                'verbose_name': 'Host_and_main_community',
                'verbose_name_plural': 'Host_and_main_communities',
            },
        ),
        migrations.CreateModel(
            name='Mentors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ProfileLink', models.URLField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('Track', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to=pathlib.PureWindowsPath('D:/Matrix_Backend/matrix/matrix_api/Mentors_images'))),
                ('Bio', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Mentor',
                'verbose_name_plural': 'Mentors',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ProfileLink', models.URLField(max_length=100)),
                ('Image', models.ImageField(upload_to=pathlib.PureWindowsPath('D:/Matrix_Backend/matrix/matrix_api/Partners_images'))),
                ('Bio', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Track', models.CharField(max_length=100)),
                ('Type_of_Speaker', models.CharField(choices=[('T', 'Talks'), ('P', 'Panels'), ('CC', 'Career Circles'), ('M', 'Mentorship'), ('W', 'Workshops')], max_length=2)),
                ('Session_Title', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('Bio', models.TextField(max_length=2000)),
                ('Image', models.ImageField(upload_to=pathlib.PureWindowsPath('D:/Matrix_Backend/matrix/matrix_api/Speaker_images'))),
                ('Profile_link', models.URLField(max_length=100)),
                ('Day', models.DateField(choices=[('2024-07-05', 'Day1'), ('2024-07-06', 'Day2'), ('2024-07-07', 'Day3')])),
                ('Time', models.TimeField()),
                ('Stage', models.CharField(choices=[('P', 'Primary'), ('S', 'Secondary'), ('W', 'Workshop'), ('M', 'Mentorship'), ('CC', 'Career Circles')], max_length=2)),
            ],
            options={
                'verbose_name': 'Speaker',
                'verbose_name_plural': 'Speakers',
            },
        ),
        migrations.CreateModel(
            name='sponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ProfileLink', models.URLField(max_length=100)),
                ('Image', models.ImageField(upload_to=pathlib.PureWindowsPath('D:/Matrix_Backend/matrix/matrix_api/sponsor_images'))),
                ('Bio', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name': 'sponsor',
                'verbose_name_plural': 'sponsors',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('scanned', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Vips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ProfileLink', models.URLField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to=pathlib.PureWindowsPath('D:/Matrix_Backend/matrix/matrix_api/Vips_images'))),
                ('Bio', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name': 'VIP',
                'verbose_name_plural': 'VIPs',
            },
        ),
    ]
