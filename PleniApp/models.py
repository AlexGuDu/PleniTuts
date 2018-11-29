from django.db import models

# Create your models here.
class Thread(models.Model):
    title = models.CharField(max_length=50)
    videourl = models.CharField(default='empty',max_length=200)
