from django.db import models

# Create your models here.
class Portofolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    language = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")
    link = models.URLField(max_length=100)