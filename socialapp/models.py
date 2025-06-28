from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Avalia(models.Model):
    id_avalia = models.AutoField(primary_key=True)
    valor_avalia = models.CharField(max_length=255)

    def __str__(self):
        return self.valor_avalia

class Postagem(models.Model):
    id_postagem = models.AutoField(primary_key=True)
    autor_postagem = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postagens')
    data_postagem = models.DateTimeField(auto_now_add=True)
    titulo_postagem = models.CharField(max_length=255)
    conteudo_postagem = models.TextField()
    id_avalia = models.ForeignKey(Avalia, models.DO_NOTHING, null=True, blank=True, db_column='id_avalia')

    def __str__(self):
        return self.titulo_postagem


class Like(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name='likes')
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'postagem')  # impede duplicatas

class Comentario(models.Model):
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)