from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

# Create your tests here.


class Testes(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(
            username="a", password="a", email="a@gmail.com")
        self.u2 = User.objects.create_user(
            username="b", password="b", email="b@gmail.com")
        self.u3 = User.objects.create_user(
            username="c", password="c", email="c@gmail.com")
    # Testes de cadstro/usuarios/tela principal

    def test_index(self):
        """verificando rota index"""
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        """verificando rota login"""
        c = Client()
        response = c.get("/login/")
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        """verificando rota register"""
        c = Client()
        response = c.get("/register/")
        self.assertEqual(response.status_code, 200)

    def test_userv(self):
        """testando quantidade de usuarios"""
        usuarios = User.objects.all()
        self.assertEqual(usuarios.count(), 3)
