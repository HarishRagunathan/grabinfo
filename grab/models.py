from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(default='image/userprofile.png', upload_to=getFileName)
    bio = models.TextField(max_length=100, blank=True)
    def __str__(self):
        return f'{self.user.username} Profile'
    
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,blank=False,null=False)
    def __str__(self):
        return self.topic_name
    
class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()
    post_image=models.ImageField(blank=False,null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Post by {self.profile.user.username} on {self.topic.topic_name}'