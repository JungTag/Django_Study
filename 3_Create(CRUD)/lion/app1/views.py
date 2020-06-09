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
    return redirect('/detail/'+str(post.id))
    # render는 최종, redirect는 throws로 넘긴