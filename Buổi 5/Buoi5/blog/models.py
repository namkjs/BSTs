from django.db import models

# Create your models here.
from django.db import models
# from stringfield import StringField

class Blog(models.Model):
    stt = models.BigIntegerField(default = 0)
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length = 200)
    content = models.TextField()    
    image = models.CharField(max_length = 300)
    class Meta:
        db_table = 'Blog1'