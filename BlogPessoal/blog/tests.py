from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .models import Categoria, Post, Comentarios
from django.utils import timezone

# Create your tests here.


class Testes(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(
            username="a", password="a", email="a@gmail.com")
        self.u2 = User.objects.create_user(
            username="b", password="b", email="b@gmail.com")
        self.u3 = User.objects.create_user(
            username="c", password="c", email="c@gmail.com")

        self.c1 = Categoria.objects.create(nome="a", usuario=self.u1)
        self.c2 = Categoria.objects.create(nome="b", usuario=self.u1)
        self.c13 = Categoria.objects.create(nome="c", usuario=self.u1)

        self.p1 = Post.objects.create(titulo="e", categoria=self.c1, dataPostagem=timezone.now(
        ), usuario=self.u1, conteudo="eeeeeeeeeeeee")
        self.p2 = Post.objects.create(titulo="f", categoria=self.c1, dataPostagem=timezone.now(
        ), usuario=self.u1, conteudo="fffffffffffff")
        self.p3 = Post.objects.create(titulo="g", categoria=self.c1, dataPostagem=timezone.now(
        ), usuario=self.u1, conteudo="ggggggggggggg")

        self.com1 = Comentarios.objects.create(
            usuario=self.u1, mensagem="mmm", postagem=self.p1)
        self.com1 = Comentarios.objects.create(
            usuario=self.u1, mensagem="nnn", postagem=self.p1)
        self.com1 = Comentarios.objects.create(
            usuario=self.u1, mensagem="ooo", postagem=self.p1)

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

    # Teste de rota categoria

    def test_categoria(self):
        """Testando rota categoria"""
        c = Client()
        response = c.get("/categoria/")
        self.assertEqual(response.status_code, 200)

    # teste de inserção de cateogira
    def test_categoriaInsert(self):
        """Testando inserção de categorias"""
        categorias = Categoria.objects.all()
        self.assertEqual(categorias.count(), 3)

    # teste de inserção de postagem
    def test_postagens(self):
        """testando isnerção de postagens"""
        postagens = Post.objects.all()
        self.assertEqual(postagens.count(), 3)

    # teste de remoção de postagem

    def test_removerPostagem(self):
        """removendo uma postagem"""
        postagem = Post.objects.get(titulo="e")
        postagem.delete()
        u1 = User.objects.get(username="a")
        postagens = Post.objects.filter(usuario=u1)
        self.assertEqual(postagens.count(), 2)

    # teste alterando postagem

    def test_alterarPostagem(self):
        """Alterando uma postagem"""
        postagem = Post.objects.get(titulo="f")
        postagem.conteudo = "zzz"
        postagem.save()
        self.assertEqual(postagem.conteudo, "zzz")

    # testando inseerção de comentários

    def test_coment_inserir(self):
        """Testando inserção de comentários"""
        comentarios = Comentarios.objects.all()
        self.assertEqual(comentarios.count(), 3)

    # testando rota de mostrar categorias

    def test_categorias(self):
        """Testando rota de mostrar categorias"""
        c = Client()
        response = c.get("/mostrarCategorias/")
        self.assertEqual(response.status_code, 200)

    # testando rota sobremim

    def test_sobremim(self):
        """Testando rota sobre mim"""
        c = Client()
        response = c.get('/apresentacao/')
        self.assertEqual(response.status_code, 200)

    # testando rota de busca por título
