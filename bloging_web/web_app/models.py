from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid

# Create your models here.
class Blogs(models.Model):
    user_id = models.CharField(max_length = 100,default='') #user_email
    title = models.CharField(max_length=100,null=True,default='')
    message = models.TextField()
    author = models.CharField(max_length=100,blank='')
    blog_img = models.ImageField(null=False,blank=False)
    Feild_area = models.IntegerField(default=0)
    #0->BUSSINESS,
    #1->TECH,
    #2->CULTURE,
    date_time = models.DateTimeField(auto_now_add=True)

    @property
    def image_url(self):
        try:
            url = self.blog_img.url
        except:
            url=''

        return url