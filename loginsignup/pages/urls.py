from django.urls import path
from . import views

urlpatterns = [
    path('',views.Loginpage,name="loginpage"),
    path('signup',views.Signuppage,name="signuppage")
]

