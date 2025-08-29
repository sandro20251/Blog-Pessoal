from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginv, name="login"),
    path('logout/', views.logoutv, name="logout"),
    path('register/', views.registerv, name="register"),
]
