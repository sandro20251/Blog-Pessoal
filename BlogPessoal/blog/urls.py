from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginv, name="login"),
    path('logout/', views.logoutv, name="logout"),
    path('register/', views.registerv, name="register"),
    path('categoria/', views.categoria, name="categoria"),
    path('post', views.post, name="post"),
    path('remover1/<int:id>', views.remover1, name="remover1"),
    path('remover2/<int:id>', views.remover2, name="remover2"),
    path('atualizarPostagem/>', views.atualizarPostagem, name="atualizarPostagem"),
    path('post/<int:id>', views.postagemView, name="postagemView"),
    path('comentario/<int:id>', views.comentario, name="comentario"),
    path('perfil/', views.perfil, name="perfil"),
    path('mostrarCategorias/', views.mostrarCategorias, name="mostrarCategorias"),
    path('categoria/<int:id>', views.postCategoria, name="postCategoria"),
    path('likes/<int:id>', views.likes, name="likes"),
    path("deslike/<int:id>", views.deslike, name="deslike"),
    path('likesPerfil<int:id>', views.likesPerfil, name="likesPerfil"),
    path('deslikePerfil/<int:id>', views.deslikePerfil, name="deslikePerfil"),
    path('likesCategoria/<int:id>', views.likesCategoria, name="likesCategoria"),
    path('deslikeCategoria/<int:id>',
         views.deslikeCategoria, name="deslikeCategoria"),
    path('likesPostagem/<int:id>', views.likesPostagem, name="likesPostagem"),
    path('deslikePostagem/<int:id>', views.deslikePostagem, name="deslikePostagem"),
    path('apresentacao/', views.apresentacao, name="apresentacao"),
    path('buscarTituloPostagem/', views.buscarTituloPostagem,
         name="buscarTituloPostagem"),

    path('atualizarPostagemPerfil/', views.atualizarPostagemPerfil,
         name="atualizarPostagemPerfil"),
    path('atualizarPostagemView/', views.atualizarPostagemView,
         name="atualizarPostagemView"),
    path('atualizarPostagemPost/', views.atualizarPostagemPost,
         name='atualizarPostagemPost')


]
