from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title= models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at =models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    
class PersonalNote(Note):   # Inherits from Note!
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
# class User(models.Model):
#     id= models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     username= models.CharField(max_length = 200, unique = True)
#     password= models.CharField(max_length = 200)
# Create your models here.
