from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=64)
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="categoriasUsuario")

    def __str__(self):
        return f"{self.nome}"


class Post(models.Model):
    titulo = models.CharField(max_length=64)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="postsCategoria")
    conteudo = models.CharField(max_length=1000)
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="postsUsuario")
    dataPostagem = models.DateTimeField()

    def __str__(self):
        return f"{self.titulo} - {self.usuario} - {self.dataPostagem}"


class Comentarios(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mesangensUsuario")
    mensagem = models.CharField(max_length=1000)
    postagem = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="p", null=True, blank=True)

    def __str__(self):
        return f"{self.mensagem}"
