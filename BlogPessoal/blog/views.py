from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Categoria, Post
from django.utils import timezone
from django.shortcuts import get_object_or_404


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        categorias = Categoria.objects.all()
        postagens = Post.objects.filter(usuario=request.user)
        return render(request, 'blog/index.html', {"categorias": categorias, "postagens": postagens})
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


def post(request):
    if request.method == "POST":
        titulo = request.POST['tituloPost']
        categoria_id = request.POST['categoriaPost']
        conteudo = request.POST['conteudoPost']
        usuario = request.user
        dataPostagem = timezone.now()
        categoria = get_object_or_404(Categoria, id=categoria_id)
        postagem = Post(titulo=titulo, categoria=categoria,
                        conteudo=conteudo, usuario=usuario, dataPostagem=dataPostagem)
        postagem.save()
        return HttpResponseRedirect(reverse('index'))


def remover1(request, id):
    postagem = Post.objects.get(pk=id)
    return render(request, 'blog/confirmarRemoverPostagem.html', {"postagem": postagem})


def remover2(request, id):
    postagem = Post.objects.get(pk=id)
    postagem.delete()
    return HttpResponseRedirect(reverse('index'))


def atualizarPostagem(request):
    if request.method == "POST":
        id = request.POST['idAtualizarPostagem']
        titulo = request.POST['tituloPostA']
        categoria = request.POST['categoriaPostA']
        categoriaObjeto = Categoria.objects.get(id=categoria)
        conteudo = request.POST['conteudoPostA']

        postagem = Post.objects.get(pk=id)
        postagem.titulo = titulo
        postagem.categoria = categoriaObjeto
        postagem.conteudo = conteudo
        postagem.save()
        return HttpResponseRedirect(reverse('index'))
