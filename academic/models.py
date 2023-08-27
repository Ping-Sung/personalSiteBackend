from django.db import models

# Create your models here.


class Academic(models.Model):
    img = models.CharField(max_length=200, default="")
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    url = models.CharField(max_length=200)
    github = models.CharField(max_length=200, default="")
    authors = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    gallary = models.TextField(default="")
