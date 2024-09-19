from django.views import View
from ..models.user import PizzaUser 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout

from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from my_pizza.settings import EMAIL_HOST_USER


class RegisterView(View):
    def get(self, request):
        return render(request, "api/register.html", {})
    
    def post(self, request):
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        address = request.POST['address']

        user = User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            username=username,
            password=password,
            email=email
        )
        user.save()
        pu = PizzaUser(user=user, phone=phone, address=address)
        
        
        
       

        # Sending confirmation email
        subject = 'Welcome to Our Service!'
        message = f'Hi {firstname},\n\nThank you for registering at our service.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)
        except Exception as e:
            print(f"Error sending email: {e}") 

        pu.save()


        return HttpResponseRedirect("login/")

        
class LoginView(View):
    def get(self, request):
        return render(request, "api/login.html", {})
    
    def post(self, request):
        usr = request.POST['username']
        pswd = request.POST['password']

        user = authenticate(username=usr, password=pswd)
        if user:
            auth_login(request, user)
            return HttpResponseRedirect("/pizza/")
        
        return render(request, "api/login.html", {"error": "Username or password is wrong"})
    
class LogOutView(View):
   def get(self, request):
        logout(request)
        return HttpResponseRedirect("/api/login")



