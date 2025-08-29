from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Categoria


# Create your views here.


def index(request):
    if request.user.is_authenticated:

        return render(request, 'blog/index.html',)
    return HttpResponseRedirect(reverse('login'))


def loginv(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        mensagem = "Não foi possível logar, tente novamente!"
        return render(request, 'blog/login.html', {"mensagem": mensagem})
    return render(request, 'blog/login.html')


def logoutv(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def registerv(request):
    if request.method == "POST":
        username = request.POST['usernameRegister']
        email = request.POST['emailRegister']
        password = request.POST['passwordRegister']
        password2 = request.POST['password2Register']

        if password != password2:
            mensagem = "As senhas não conferem, digite de novo!"
            return render(request, 'blog/login.html', {"mensagem": mensagem})
        registro = User.objects.create_user(
            username=username, password=password, email=email)
        registro.save()
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'blog/register.html')


def categoria(request):
    if request.method == "POST":
        nome = request.POST['categoriaCategoria']
        usuario = request.user
        categoria = Categoria(nome=nome, usuario=usuario)
        categoria.save()
        return HttpResponseRedirect(reverse('categoria'))
    categorias = Categoria.objects.all()
    return render(request, 'blog/categoria.html', {"categorias": categorias})
