from django.db import models

# Create your models here.
class Lecture(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default='empty')
    videourl = models.CharField(default='tgbNymZ7vqY', max_length=200)
    unit_index = models.IntegerField(default=0)
    lecture_type_index = models.IntegerField(default=0)
    lecture_index_number = models.IntegerField(default=0)
    navlinkid = models.CharField(default='navlink_' ,max_length=20)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=20, default='regular')

    def __str__(self):
        return "%s %s" % (self.username)


class Comment(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

class Reply(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
