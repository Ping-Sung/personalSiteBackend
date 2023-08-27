from django.db import models

# Create your models here.


class Experience(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default='')
    company = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    description = models.TextField()
    gallary = models.ImageField(upload_to='experience/images', default='')
    urls = models.URLField(max_length=200, default='')
    skills = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.title
