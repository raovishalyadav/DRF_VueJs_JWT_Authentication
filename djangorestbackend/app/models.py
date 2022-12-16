from django.db import models

class Apicrud(models.Model):
    first = models.CharField(max_length=300,blank=True)
    second = models.DateTimeField(auto_now_add=True)
    third = models.IntegerField(default=0)
    fourth = models.EmailField(max_length=254,blank=True)
    fifth = models.BooleanField(default=False)
    sixth = models.ImageField(upload_to="images/",blank=True)
    seventh = models.FileField(upload_to="files/",blank=True)
    eight = models.TextField(blank=True)
    STATUS_CHOICES = ( 
    ('TODO','TODO'),
    ('DONE','DONE')
    )
    nine = models.CharField(max_length=4,choices=STATUS_CHOICES,default=STATUS_CHOICES[0][0]) 
    
    class Meta:   
        #ordering as shown in the API
        ordering = ['second']
        

# from django.contrib.auth.models import AbstractUser


# # Create your models here.
# class User(AbstractUser):
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     username = None

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []