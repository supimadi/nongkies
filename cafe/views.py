from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from .models import Cafes, Reviewer, CafeReview

def home_page(request):
    ctx = {
        "cafes": Cafes.objects.all(),
    }

    return render(request, "cafe/home.html", ctx)

def cafe_detail(request, pk):

    cafe = get_object_or_404(Cafes, pk=pk)
    cafe_review = CafeReview.objects.filter(cafe=cafe)

    ctx = {
        "cafe": cafe,
        "cafe_review": cafe_review
    }

    return render(request, "cafe/cafe_detail.html", ctx)

@login_required
def user_profile(request):
    reviewer = Reviewer.objects.get(account=request.user.pk)
    reviewed_cafe = CafeReview.objects.filter(user=reviewer)

    ctx = {
        "reviewer": reviewer,
        "reviewed_cafe": reviewed_cafe
    }

    return render(request, "cafe/user_profile.html", ctx)

def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()

        user = authenticate(
            request, username=form.cleaned_data["username"],
            password=form.cleaned_data["password2"]
        )
        login(request, user)

        return redirect('profile')

    return render(request, "cafe/register.html", {"form": form})

class LoginUser(LoginView):
    template_name = "cafe/login.html"

class LogoutUser(LogoutView):
    template_name = "cafe/logout.html"

class UpdateProfileView(UserPassesTestMixin, UpdateView):
    model = Reviewer
    template_name = "cafe/update_profile.html"
    success_url = reverse_lazy("profile")
    fields = ["bio", "picture"]

    def test_func(self):
        profile = Reviewer.objects.get(pk=self.kwargs["pk"])

        if profile.account.pk == self.request.user.pk:
            return True
        else:
            return False

