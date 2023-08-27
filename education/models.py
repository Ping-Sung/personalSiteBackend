from django.db import models

# Create your models here.


class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    gpa = models.CharField(max_length=100)
    badge = models.CharField(max_length=100)
    degrees = models.CharField(max_length=100, default="")
