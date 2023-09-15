from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from .forms import BlogForm
from .forms import ImageUploadForm
from .models import Blog
from PIL import Image
from io import StringIO
from datetime import date
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

@csrf_exempt
def create_blog(request):
    form = BlogForm()  # Khởi tạo form
    if request.method == "POST":
        id = request.POST['id']
        title = request.POST['title']
        content = request.POST['content']
        today = date.today()
        image = f'/media/{id}.png'
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['image'], id)
        # Tạo một instance của Blog với dữ liệu từ form
        blog = Blog(id=id, title=title, content=content, date = today, image = image)
        blog.save()  # Lưu blog vào cơ sở dữ liệu
    return render(request, 'app/create.html', {'form': form})
def handle_uploaded_file(f, id):
    fs = FileSystemStorage()
    # f.save(f'/blog/static/images/{id}.jpg', 'JPEG')
    filename = fs.save(f'{id}.png', f)

def home(request):
    return render(request, "app/home.html")
@csrf_exempt
def table(request):
    data = Blog.objects.all()
    return render(request, 'app/read.html', {'data': data})
    
@csrf_exempt
def update_blog(request):
    if request.method == "POST":
        ID = request.POST['id']
        x = Blog.objects.get(id=ID)
        if (request.POST['title'] != ""):
            x.title = request.POST['title']
            x.save()
        if (request.POST['content'] != ""):
            x.content = request.POST['content']
            x.save()
        x.date = date.today()
        x.save()
    return render(request, 'app/update.html')
@csrf_exempt
def delete_blog(request, id):
    blogs = Blog.objects.get(id=id)
    blogs.delete()
    return redirect("/read")


def view_blog(request, id):
    number = id
    blogs = Blog.objects.get(id=id)
    return redirect(f'/view/{id}')

def read_blog(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'app/view.html', {'data': blog})