from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('Login', views.login, name="Login"),
    path('Register', views.register, name="Register"),
]
