from django.db import models
from PIL import Image
from django.contrib.auth.models import User  # Adicione esta importação
from socialapp.models import Postagem  # Certifique-se que Postagem está definido em socialapp.models

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  # Relação com User
    nome_perfil = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    matricula_perfil = models.CharField(max_length=255)
    foto_perfil = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True)  # Adicione upload_to

    def __str__(self):
        return self.nome_perfil

    def save(self, *args, **kwargs):  # Corrigido o método save
        super().save(*args, **kwargs)
        if self.foto_perfil:  # Só redimensionar se houver imagem
            try:
                im = Image.open(self.foto_perfil.path)
                novo_tamanho = (100, 100)
                im.thumbnail(novo_tamanho)
                im.save(self.foto_perfil.path)
            except:
                pass

    def foto_url(self):
        if self.foto_perfil and hasattr(self.foto_perfil, 'url'):
            return self.foto_perfil.url
        return '/static/images/default_profile.png'  # Imagem padrão se não houver foto

class Telefone(models.Model):
    numero_telefone = models.CharField(max_length=20)  # Tamanho reduzido para números de telefone
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='telefones')

    def __str__(self):
        return self.numero_telefone

class PerfilPost(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    data_associacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('perfil', 'postagem')

    def __str__(self):
        return f"{self.perfil} - {self.postagem}"