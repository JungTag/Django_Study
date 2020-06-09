from django.db import models

# Create your models here.
class Post(models.Model):
    "id/pk = int => 각 게시물의 고유한 번호를 배정해준다."
    title = models.CharField(max_length = 20)
    # title이라는 열을 만들고 models -> Char(제한적 길이를 가진 문자) -> max_length
    body = models.TextField() 
    # body라는 열을 만들고 Text(제한이 없는 문자열)
    pub_date = models.DateTimeField('published time') # 파라미터 -> 소제목
    # pub_date라는 열을 만들고, 그 형식을 날짜/시간 형태로 넣겠다.
    
    def __str__(self):
        return self.title
    