from django.shortcuts import render
from .models import Post

def index(request):
    
    result = Post.objects.all() 
    # Post.objects -> 게시물 객체들
    # Post.objects.all() -> 게시물 행들을 List로 가져와준다. -> 메소드(객체를 다루는 함수들)
    # .filter(), .order_by() -> 메소드
    # 쿼리셋 -> 쿼리(요청) -> Set(가져와준다) 쿼리셋이라고 부른다!
    print(result)
    return render(request, 'index.html', {"post_list" : result})

def detail(request, num, title): 
    # 두 번째 매개변수는 키워드로 넘겨주기 때문에 urls.py에서 정의해준 것과 동일해야한다.
    content = Post.objects.get(title=title) # 행 id가 num인 것을 1개 넘겨준다.
    Post.objects.filter(writer = writer) # 값이 리스트로 넘어옴 => 여러개를 추출해줌
    return render(request, 'detail.html', {'content': content})

# Create your views here.
