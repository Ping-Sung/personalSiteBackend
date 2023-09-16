from django.db import models

# Create your models here.


def upload_to(instance, filename):
    return 'images/experience/%s' % filename


class Experience(models.Model):

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100)
    description = models.TextField()
    urls = models.URLField(max_length=200, default='')
    skills = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.title


class gallery(models.Model):
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    experience = models.ForeignKey(
        Experience, on_delete=models.CASCADE, related_name='gallery')

    def __str__(self):
        return self.experience.title
