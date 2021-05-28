
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField

class AcceptedpostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=50 ,default="")

    def __str__(self):
          return self.catagory_name


class post(models.Model):
    post_id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=255 ,default="")
    author =models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=130)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    thumbnail = models.ImageField(upload_to='shop/images', default="")
    status=models.BooleanField(default="True")

    content = HTMLField()
    acceptpost = AcceptedpostManager()
    objects =models.Manager()

    def __str__(self):
        return self.title



# Create your models here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email