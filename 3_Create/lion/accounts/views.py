from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Signup

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'], password= request.POST['password1']
            )
            signup = Signup()
            signup.major = request.POST['major']
            signup.phone = request.POST['phone']
            signup.user = user
            signup.save()
            auth.login(request, user)         
            return redirect('index')
    return render(request, 'signup.html') # {% url 'signup' %}

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password) 
        # 진위여부 판단(request가 들어올 때)

        if user is not None: # 유저가 존재
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error' : "username or password is not correct"})
    else: 
        return render(request, 'login.html')

def logout(request):
    auth.logout(request) 
    # user가 request 안에 존재하기 때문에 따로 안 넘겨줘도 됨!!
    return redirect('/')

def profile(request):
    user = request.user
    sign = Signup.objects.get(user=user)
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            sign.phone = request.POST['phone']
            sign.major = request.POST['major']
            user.set_password(request.POST['password1'])
            sign.save()
            user.save()
            return redirect('/')
    return render(request, 'profile.html', {'profile':sign})


