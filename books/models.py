from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)  
    email = models.EmailField(unique=True)
    user_id = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=128,default='')

    def __str__(self):
        return f"{self.email} {self.name}"


class Role(models.Model):
    role_name = models.CharField(max_length=30,default='')
    email = models.EmailField(unique=True,default='')

    def __str__(self):
        return f"{self.email} {self.role_name}"
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title

