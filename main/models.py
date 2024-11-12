from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    project_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFit(400, 300)],
                                     format='JPEG',
                                     options={'quality': 90})

    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    linkedin = models.URLField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    responsibilities = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"


class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.email
