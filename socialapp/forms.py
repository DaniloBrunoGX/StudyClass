from django import forms
from socialapp.models import Avalia, Postagem, Comentario

class AvaliaForms(forms.ModelForm):
    class Meta:
        model = Avalia
        fields ="__all__"


class PostagemForms(forms.ModelForm):
    class Meta:
        model = Postagem
        exclude = ['autor_postagem', 'data_postagem']


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite um comentário...'})
        }