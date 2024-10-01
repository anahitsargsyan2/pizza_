from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.basket import Basket
from ..models.drinks import Drinks
from ..models.pizza import Pizza
import re

class BasketView(LoginRequiredMixin, View):
    def post(self, request):
        action = request.POST.get('action')
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity', 1)

        
        if not product_id:
            return JsonResponse({'error': 'Product ID is required'}, status=400)

        try:
            quantity = int(quantity)
            if quantity <= 0:
                return JsonResponse({'error': 'Quantity must be greater than zero'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'Quantity must be a number'}, status=400)

      
        basket, created = Basket.objects.get_or_create(user=request.user)

        if action == "add":
            self.add_product_to_basket(basket, product_id, quantity)
        elif action == "remove":
            self.remove_product_from_basket(basket, product_id, quantity)
        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)

        basket.save()

        total_sum = self.calculate_total(basket)
        total_quantity = basket.pizzas.count() + basket.drinks.count()
        items_summary = {}
        for pizza in basket.pizzas.all():
            items_summary[pizza.title] = basket.pizzas.filter(id=pizza.id).count()
        for drink in basket.drinks.all():
            items_summary[drink.title] = basket.drinks.filter(id=drink.id).count()
        return JsonResponse({'total_sum': total_sum, 'quantity': total_quantity, 'items': items_summary})

    def get(self, request):
        items = []
        
      
        for pizza in Basket.pizzas.all():
            items.append({
                'name': pizza.name,
                'quantity': pizza.quantity, 
                'price': pizza.price 
            })

  
        for drink in Basket.drinks.all():
            items.append({
                'name': drink.name,
                'quantity': drink.quantity,  
                'price': drink.price  
            })

        return items

    def add_product_to_basket(self, basket, product_id, quantity):
        pizza = Pizza.objects.filter(id=product_id).first()
        if pizza:
            for _ in range(quantity):
                basket.pizzas.add(pizza)

        drink = Drinks.objects.filter(id=product_id).first()
        if drink:
            for _ in range(quantity):
                basket.drinks.add(drink)



    def remove_product_from_basket(self, basket, product_id, quantity):
        pizza = Pizza.objects.filter(id=product_id).first()
        if pizza:
            for _ in range(min(quantity, basket.pizzas.filter(id=pizza.id).count())):
                basket.pizzas.remove(pizza)

    def calculate_total(self, basket):
        total = 0
        for pizza in basket.pizzas.all():
            price_str = pizza.price
            price_cleaned = re.sub(r'[^\d.]', '', price_str)
            total += float(price_cleaned)  
        
        for drink in basket.drinks.all():
            price_str = drink.price
            price_cleaned = re.sub(r'[^\d.]', '', price_str)
            total += float(price_cleaned)
        
        
        return total

    