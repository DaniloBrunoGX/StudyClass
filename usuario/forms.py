from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from usuario.models import Perfil, Telefone, PerfilPost
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from datetime import date


class UsuarioForm(UserCreationForm):
    FIRST_NAME_CHOICES = [
        ('Docente','Docente'),
        ('Discente','Discente')
    ]
    class Meta:
        model=User
        fields =['username','email','last_name','first_name']
    username = forms.CharField(label='Matrícula:')
    email = forms.EmailField(label='E-mail:')
    last_name = forms.CharField(label='Nome Completo:')
    first_name = forms.ChoiceField(
        label='Status:',
        choices=FIRST_NAME_CHOICES,
        widget=forms.Select(attrs={'class':'custom-select'}),
        initial='Discente'
    )



class PerfilForms(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = "__all__"
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'foto_perfil': forms.FileInput(attrs={'accept': 'image/*'})
        }
    
    def clean_data_nascimento(self):
        data_nasc = self.cleaned_data['data_nascimento']
        idade = (date.today() - data_nasc).days // 365
        if idade < 13:
            raise ValidationError("Você deve ter pelo menos 13 anos para se registrar.")
        return data_nasc

class TelefoneForms(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = "__all__"
        widgets = {
            'numero_telefone': forms.TextInput(attrs={
                'placeholder': '(00) 00000-0000',
                'pattern': '\([0-9]{2}\) [0-9]{5}-[0-9]{4}'
            })
        }

class PerfilPostForms(forms.ModelForm):
    class Meta:
        model = PerfilPost
        fields = "__all__"
        widgets = {
            'id_perfil': forms.Select(attrs={'class': 'form-select'}),
            'id_postagem': forms.Select(attrs={'class': 'form-select'})
        }