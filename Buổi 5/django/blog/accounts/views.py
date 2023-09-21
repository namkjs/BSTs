from django.shortcuts import render, redirect
from .models import Blogs
from .forms import BlogForm , CustomUserRegister
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
# Create your views here.



def registerPage(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in")
        return redirect('/')
    else:
        form = CustomUserRegister()
        if request.method == 'POST':
            form = CustomUserRegister(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Register successfully!")
                return redirect('blogs')
        context = {'form': form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in")
        return redirect('/')
    else:
        if request.method == 'POST':
            loginusername = request.POST.get('username')
            loginpassword = request.POST.get('password')
            
            user = authenticate(request, username=loginusername, password=loginpassword)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('/')
        
        return render(request, 'accounts/login.html')

def logoutPage(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('/')
    

def home(request):
    return render(request, 'accounts/index.html')

def blogs(request):
    form = Blogs.objects.all()
    context = {'form': form}
    return render(request, 'accounts/index.html', context)

def viewblog(request, pk):
    blogs = Blogs.objects.get(id=pk)
    context = {'blogs': blogs}
    return render(request, 'accounts/view.html', context)

def addblog(request):
    form = BlogForm
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Blog added successfully")
            return redirect('blogs')
    context = {'form': form}
    return render(request, 'accounts/add.html', context)
  
def editBlog(request, pk):
    blog_id = Blogs.objects.get(id=pk)
    form = BlogForm(instance = blog_id)
    
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES, instance=blog_id)
        if form.is_valid():
            form.save()
            messages.success(request,"Blog updated successfully")
            return redirect('blog')
    context = {'form': form}
    return render(request, 'accounts/edit.html', context)

def deleteBlog(request,pk):
    form = Blogs.objects.get(id=pk)
    form.delete()
    messages.success(request,"Blog deleted successfully")
    return redirect('blogs')