from django.db import models

# Create your models here.
class Blog(models.Model):
    uname = models.CharField(max_length=64)
    post = models.CharField(max_length=2000)