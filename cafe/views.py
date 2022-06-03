from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.views import LoginView

from .models import Cafes

def home_page(request):
    ctx = {
        "cafes": Cafes.objects.all(),
    }

    return render(request, "cafe/home.html", ctx)

def user_profile(request):
    return render(request, "cafe/user_profile.html")

class LoginUser(LoginView):
    template_name = "cafe/login.html"
    success_url = reverse_lazy('home')
