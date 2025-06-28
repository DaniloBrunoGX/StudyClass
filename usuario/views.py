from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import UsuarioForm
from django.contrib import messages
from django.contrib.auth import logout
from django.views import View


# Create your views here.
def new_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
    else:
        form = UsuarioForm()  # Form vazio para GET requests
    
    return render(request, 'usuario/usuario.html', {'form': form})


class LogoutGetView(View):
    def get(self, request):
        logout(request)
        return redirect('login')