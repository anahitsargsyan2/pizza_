"""
URL configuration for my_pizza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .api.pizza import PizzaView
from .api.drinks import DrinksView
from .api.User import RegisterView, LoginView, LogOutView
from .api.basket import BasketView

urlpatterns = [
    path("pizzerias/", include("pizzerias.urls")),
    path('admin/', admin.site.urls),
    path('pizza/', PizzaView.as_view()),
    path('drinks/', DrinksView.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogOutView.as_view()),
    path('basket', BasketView.as_view(), name="basket"),
]
