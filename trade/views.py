from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'trade/index.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'trade/home.html')

def demo(request):
    return render(request, 'trade/demo.html')

def signup(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            # print('Passwords cannot be same')
            return redirect('signup')
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render(request, 'trade/signup.html')

def my_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass')

        user=authenticate(request, username=username, email=email, password=pass1)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request, 'trade/login.html')

def my_logout(request):
    logout(request)
    return redirect('login')