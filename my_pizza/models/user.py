from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class PizzaUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)


    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
    
    

@admin.register(PizzaUser)
class PizzaUserAdmin(admin.ModelAdmin):
    pass