from django.db import models
from django.contrib.auth.models import User


class PizzeriasUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)


    def __str__(self):
        return "{} {}".format(self.name)
    

class Product(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=100) 
    image_url = models.URLField()  
