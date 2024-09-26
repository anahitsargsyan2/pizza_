from django.contrib import admin
from .models import PizzeriasUser, Product



admin.site.register(PizzeriasUser, Product)
