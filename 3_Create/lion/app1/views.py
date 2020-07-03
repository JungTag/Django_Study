from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
# Create your views here.
def index(request):
    my_post = Post.objects.all()
    return render(request, 'index.html', {'all_post': my_post})

def detail(request, id):
    result = Post.objects.get(id = id)
    return render(request, 'detail.html', {'content': result})

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save() 
    # save를 마지막에 해야 데이터의 일관성이 유지됨!!
    return redirect('/detail/' + str(post.id))
    # render는 최종, redirect는 throws로 넘긴다.

def update(request, num): # 매개변수명이 url이랑 같아야 한다.
    post = Post.objects.get(id=num)
    if request.method == "POST":
        # 수정된 글을 저장해주겠다.
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
        return redirect('/detail/' + str(post.id))
    # 수정할 글을 보내주겠다.
    return render(request, 'update.html', {"result" : post})

def delete(request, num):
    post = Post.objects.get(id=num)
    post.delete()
    return redirect('/') # home -> url이 없는 것을 의미

def album(request):
    img = Album.objects.all()
    return render(request, 'album.html', {"imgs" : img})