import os
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
from accounts.models import Profile

def GetImageUploadTo(instance, ImageName):
    name, ext = os.path.splitext(ImageName)
    id = uuid4()
    return f"Posts/{id}{ext}"

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=4000)
    PostImg = models.ImageField(upload_to=GetImageUploadTo)
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    def save(self): 
        id = uuid4()
        self.slug = slugify(self.title) +'-'+str(id)
        super().save()  
    
    def __str__(self):
        return self.title   

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user.username)    