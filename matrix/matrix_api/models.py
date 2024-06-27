from django.db import models
from django.conf import settings


class user(models.Model):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    email = models.EmailField(max_length=100, primary_key=True)
    scanned = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class sponsors (models.Model):
    class Meta:
        verbose_name = 'sponsor'
        verbose_name_plural = 'sponsors'
    name = models.CharField(max_length=100)
    ProfileLink = models.URLField(max_length=100)
    Image = models.ImageField(
        upload_to=settings.BASE_DIR / 'matrix_api/sponsor_images/')
    Bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Communities_Partners (models.Model):
    class Meta:
        verbose_name = 'Community_Partner'
        verbose_name_plural = 'Communities_Partners'
    name = models.CharField(max_length=100)
    ProfileLink = models.URLField(max_length=100)
    Image = models.ImageField(
        upload_to=settings.BASE_DIR / 'matrix_api/Communities_Partners_images/')
    Bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Partners (models.Model):
    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
    name = models.CharField(max_length=100)
    ProfileLink = models.URLField(max_length=100)
    Image = models.ImageField(
        upload_to=settings.BASE_DIR / 'matrix_api/Partners_images/')
    Bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Vips (models.Model):
    class Meta:
        verbose_name = 'VIP'
        verbose_name_plural = 'VIPs'
    name = models.CharField(max_length=100)
    ProfileLink = models.URLField(max_length=100)
    position = models.CharField(max_length=100)
    Image = models.ImageField(
        upload_to=settings.BASE_DIR / 'matrix_api/Vips_images/')
    Bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Mentors (models.Model):
    class Meta:
        verbose_name = 'Mentor'
        verbose_name_plural = 'Mentors'
    name = models.CharField(max_length=100)
    ProfileLink = models.URLField(max_length=100)
    position = models.CharField(max_length=100)
    Track = models.CharField(max_length=100)
    Image = models.ImageField(
        upload_to=settings.BASE_DIR / 'matrix_api/Mentors_images/')
    Bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Speaker (models.Model):
    class Meta:
        verbose_name = 'Speaker'
        verbose_name_plural = 'Speakers'

    class Speaker_Types(models.TextChoices):
        Talks = 'T'
        Panels = 'P'
        Career_Circles = 'CC'
        Mentorship = 'M'
        Workshops = 'W'

    class Day (models.TextChoices):
        Day1 = '2024-07-05'
        Day2 = '2024-07-06'
        Day3 = '2024-07-07'

    class stages (models.TextChoices):
        Primary = 'P'
        Secondary = 'S'
        Workshop = 'W'
        Mentorship = 'M'
        Career_Circles = 'CC'

    name = models.CharField(max_length=100)
    Track = models.CharField(max_length=100)
    Type_of_Speaker = models.CharField(
        choices=Speaker_Types.choices, max_length=2)
    Session_Title = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Bio = models.TextField(max_length=2000)
    Image = models.ImageField(
        upload_to=settings.BASE_DIR / 'matrix_api/Speaker_images/')
    Profile_link = models.URLField(max_length=100)
    Day = models.DateField(choices=Day.choices)
    Time = models.TimeField()
    Stage = models.CharField(max_length=2, choices=stages.choices)

    def __str__(self):
        return self.name


class Host_and_main_communities (models.Model):
    class Meta:
        verbose_name = 'Host_and_main_community'
        verbose_name_plural = 'Host_and_main_communities'

    class Types (models.TextChoices):
        Host = 'H'
        Main_Community = 'MC'
    name = models.CharField(max_length=100)
    community_type = models.CharField(max_length=2, choices=Types.choices)
    ProfileLink = models.URLField(max_length=100)
    Image = models.ImageField(
        upload_to=settings.BASE_DIR / 'matrix_api/Host_and_main_communities_images/')

    def __str__(self):
        return self.name
