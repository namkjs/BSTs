from django.db import models
from django.db.models.deletion import SET_DEFAULT, SET_NULL
import datetime
import os
# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=191, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name
    
def filepath(request, filename):  
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H;%M:%S')
    filename = "%s%s" % (timeNow,old_filename)
    return os.path.join('uploads/',filename)
    
class Item(models.Model):
    name = models.TextField(max_length=191)
    price = models.TextField(max_length=50)
    description = models.TextField(max_length=500,null = True)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    
    
def get_filename(instance,filename):
    old_name = filename
    current_time = datetime.datetime.now().strftime('%Y%m%d%H;%M:%S')
    filename = "%s%s" % (current_time,old_name)
    return os.path.join('uploads/',filename)
    
                                                    
class Blogs(models.Model):
    category = models.ForeignKey("BlogCategory", on_delete= SET_NULL, null = True)                       
    title = models.CharField(max_length=191, null = True)
    description = models.CharField(max_length=500, null = True)
    image = models.ImageField(upload_to=get_filename, null = True, blank = True)
    create_at = models.DateTimeField(auto_now_add=True, null = True)
    
    
    def __str__(self):
        return self.title