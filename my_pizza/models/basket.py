from django.db import models
from django.contrib import admin
from .pizza import Pizza
from .drinks import Drinks
from .user import PizzaUser
from django.contrib.auth.models import User

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pizzas = models.ManyToManyField(Pizza, blank=True)
    drinks = models.ManyToManyField(Drinks, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.drinks

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass