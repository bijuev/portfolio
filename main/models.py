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
                                     processors=[ResizeToFit(200, 150)],
                                     format='JPEG',
                                     options={'quality': 80})

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
