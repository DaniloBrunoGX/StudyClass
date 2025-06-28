from django.urls import path
from .views import index, sobre, postar, contato, new_avalia, editar_avalia, deleta_avalia
from .views import new_post, deleta_post, editar_post, curtir_postagem

urlpatterns = [
    path('index/', index, name='index'),
    path('sobre/', sobre, name='sobre'),
    path('postar/', postar, name='postar'),
    path('contato/', contato, name='contato'),
    path('new_avalia/', new_avalia, name='new_avalia'),
    path('editar_avalia/<str:id>', editar_avalia, name='editar_avalia'),
    path('deleta_avalia/<int:id>', deleta_avalia, name='deleta_avalia'),
    #post
    path('', new_post, name='new_post'),
    path('editar_post/<str:id>', editar_post, name='editar_post'),
    path('deleta_post/<int:id>', deleta_post, name='deleta_post'),
    
    # nova rota de curtida:
    path('curtir/<int:id_postagem>/', curtir_postagem, name='curtir_postagem'),
]