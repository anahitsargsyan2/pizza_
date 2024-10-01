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
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Basket of {self.user.username} with {self.pizzas.count()} pizzas and {self.drinks.count()} drinks'

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass