from django.db import models

# Create your models here.
class Lecture(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    videourl = models.CharField(default='empty',max_length=200)
    unit_index = models.IntegerField()
    lecture_type_index = models.IntegerField()
