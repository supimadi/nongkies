from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home_page, name="home-page"),

    # Authentication route
    path('login/', views.LoginUser.as_view(), name="login"),
    path('logout/', views.LogoutUser.as_view(), name="logout"),
    path('register/', views.register, name="register"),

    path('cafe/detail/<int:pk>/', views.cafe_detail, name="cafe-detail"),

    path('profile/', views.user_profile, name="profile"),
    path('profile/update/<int:pk>/', views.UpdateProfileView.as_view(), name="update-profile"),
]
