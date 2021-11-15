from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('Title', max_length=100)
    asda  = models.CharField('asd', max_length=100, default="Adf")