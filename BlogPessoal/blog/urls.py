from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginv, name="login"),
    path('logout/', views.logoutv, name="logout"),
    path('register/', views.registerv, name="register"),
    path('categoria/', views.categoria, name="categoria"),
    path('post/', views.post, name="post"),
    path('remover1/<int:id>', views.remover1, name="remover1"),
    path('remover2/<int:id>', views.remover2, name="remover2"),
]
