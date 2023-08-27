from django.db import models

# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    # date is default to the current date
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    