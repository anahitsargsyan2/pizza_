from ..models.basket import Basket
from ..models.drinks import Drinks
from ..models.pizza import Pizza
from ..models.user import PizzaUser
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseForbidden

from django.contrib.auth.mixins import LoginRequiredMixin

class BasketView(LoginRequiredMixin, View):
    def post(self, request):
        action = request.POST.get('action')
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        # Check if the basket exists or create a new one
        basket, created = Basket.objects.get_or_create(user=request.user)

        if action == "add":
            self.add_product_to_basket(basket, product_id, quantity)
        elif action == "remove":
            self.remove_product_from_basket(basket, product_id, quantity)

        basket.save()

        total_sum = self.calculate_total(basket)
        total_quantity = basket.pizzas.count() + basket.drinks.count()

        return JsonResponse({'total_sum': total_sum, 'quantity': total_quantity})

    def get(self, request):
       


        basket, created = Basket.objects.get_or_create(user=request.user)
        total_sum = self.calculate_total(basket)
        return render(request, 'api/basket.html', {'basket': basket, 'total_sum': total_sum})

    def add_product_to_basket(self, basket, product_id, quantity):
        if Pizza.objects.filter(id=product_id).exists():
            pizza = get_object_or_404(Pizza, id=product_id)
            basket.pizzas.add(pizza)

        elif Drinks.objects.filter(id=product_id).exists():
            drink = get_object_or_404(Drinks, id=product_id)
            basket.drinks.add(drink)

    def remove_product_from_basket(self, basket, product_id, quantity):
        if Pizza.objects.filter(id=product_id).exists():
            pizza = get_object_or_404(Pizza, id=product_id)
            basket.pizzas.remove(pizza)

        elif Drinks.objects.filter(id=product_id).exists():
            drink = get_object_or_404(Drinks, id=product_id)
            basket.drinks.remove(drink)

    def calculate_total(self, basket):
        total = 0
        if basket:
            for pizza in basket.pizzas.all():
                total += pizza.price  # Ensure that price field exists
            for drink in basket.drinks.all():
                total += drink.price  # Ensure that price field exists
        return total
