from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE) # 1:n 관계를 표현
    '''
    1 : n -> n : 1, n을 담당하는 테이블에 연결을 해줘야 한다.
    Post(n)에 유저(1)를 연결
    '''
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

class Album(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to="album/") # media 폴더 안에 album 폴더를 만들고 거기에 넣어줘

    def __str__(self):
        return self.title