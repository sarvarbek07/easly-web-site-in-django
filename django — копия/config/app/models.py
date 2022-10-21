from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField,DateTimeField

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    image=models.ImageField(upload_to='media/images',blank=True)
    ontime=models.DateTimeField(auto_now_add=True)
    after=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    # class Meta:
    #     ordering=['-updated','-created']

    def __str__(self) :
        return self.title                                                                   




class Card(models.Model):
    img=models.ImageField(upload_to='media/images',blank=True )
    tit=models.CharField(max_length=200)
    body=models.TextField()