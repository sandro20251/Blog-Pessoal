from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=64)
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="categoriasUsuario")

    def __str__(self):
        return f"{self.nome}"
