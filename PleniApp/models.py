from django.db import models

# Create your models here.
class Lecture(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default='empty')
    videourl = models.CharField(max_length=200)
    unit_index = models.IntegerField(default=0)
    lecture_type_index = models.IntegerField(default=0)
