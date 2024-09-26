from django.db import models
from django.contrib import admin
from ..models.user import PizzaUser
from django.utils import timezone


class ToppingGroup(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title
    

class Topping(models.Model):
    topping_group = models.ForeignKey(ToppingGroup, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title}, {self.price}"
    

class Order(models.Model):
    user = models.ForeignKey(PizzaUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    topping = models.ManyToManyField(Topping)

    def total_price(self):
        return sum(topping.price for topping in self.topping.all())
    
    def __str__(self) -> str:
        return f"order by {self.user} in {self.created_at} /n total sum :{self.total_price}"
    

    

@admin.register(ToppingGroup)
class ToppingGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass