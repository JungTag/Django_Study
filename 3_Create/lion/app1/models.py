from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

class Album(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to="album/") # media 폴더 안에 album 폴더를 만들고 거기에 넣어줘

    def __str__(self):
        return self.title