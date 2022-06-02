from django.shortcuts import render
from django.contrib.auth.views import LoginView

def home_page(request):
    return render(request, "cafe/home.html")

class LoginUser(LoginView):
    template_name = "cafe/login.html"

