

from django.shortcuts import render, redirect, get_object_or_404
from socialapp.forms import AvaliaForms,PostagemForms, ComentarioForm
from socialapp.models import Avalia, Postagem, Like
from usuario.forms import UsuarioForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    postagens =Postagem.objects.all()
    return render(request, 'base/base.html', {'postagens':postagens})

def contato(request):
    return render(request, 'base/contact.html')

def sobre(request):
    return render(request, 'base/about.html')

def postar(request):
    return render(request, 'base/post.html')

def new_avalia(request):
    avas = Avalia.objects.all()
    form = AvaliaForms()
    if request.method=='POST':
        form =AvaliaForms(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            form= AvaliaForms()
    return render(request, 'avaliação/new_avalia.html', {'form':form, 'avas':avas})

def editar_avalia(request, id):
    avaliado =get_object_or_404(Avalia, pk=id)
    form =AvaliaForms(instance=avaliado)
    avas =Avalia.objects.all()

    if(request.method =="POST"):
        form = AvaliaForms(request.POST, request.FILES, instance=avaliado)
        if form.is_valid():
            form.save()
            return redirect('new_avalia')
        return render(request, 'avaliação/editar_avalia.html', {'form': form, 'avas': avas, 'avaliado':avaliado})
    else:
        return render(request, 'avaliação/editar_avalia.html',{'form': form, 'avas': avas, 'avaliado': avaliado})



def deleta_avalia(request,id):
    avaliado = get_object_or_404(Avalia, pk=id)
    form = AvaliaForms(instance=avaliado)
    avas = Avalia.objects.all()
    if request.method == "POST":
        avaliado.delete()
        return redirect('new_avalia')
    return render(request,'avaliação/deleta_avalia.html',{'avaliado':avaliado, 'form':form, 'avas':avas})

@login_required
def new_post(request):
    posts = Postagem.objects.all().order_by('-data_postagem')
    form = PostagemForms()
    comentario_form = ComentarioForm()

    if request.method == 'POST':
        if 'submit_postagem' in request.POST:
            form = PostagemForms(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.autor_postagem = request.user
                obj.save()
                return redirect('new_post')

        elif 'submit_comentario' in request.POST:
            comentario_form = ComentarioForm(request.POST)
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Postagem, id_postagem=post_id)
            if comentario_form.is_valid():
                comentario = comentario_form.save(commit=False)
                comentario.autor = request.user
                comentario.postagem = post
                comentario.save()
                return redirect('new_post')

    return render(request, 'post/new_post.html', {
        'form': form,
        'posts': posts,
        'comentario_form': comentario_form
    })

def editar_post(request, id):
    post =get_object_or_404(Postagem, pk=id)
    form =PostagemForms(instance=post)
    posts =Postagem.objects.all()

    if(request.method =="POST"):
        form = PostagemForms(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('new_post')
        return render(request, 'post/editar_post.html', {'form': form, 'posts': posts, 'post':post})
    else:
        return render(request, 'post/editar_post.html', {'form': form, 'posts': posts, 'post':post})



def deleta_post(request,id):
    post = get_object_or_404(Postagem, pk=id)
    form = PostagemForms(instance=post)
    posts = Postagem.objects.all()
    if request.method == "POST":
        post.delete()
        return redirect('new_post')
    return render(request,'post/deleta_post.html',{'post':post, 'form':form, 'posts':posts})


@login_required
def curtir_postagem(request, id_postagem):
    postagem = get_object_or_404(Postagem, pk=id_postagem)
    like, created = Like.objects.get_or_create(usuario=request.user, postagem=postagem)
    if not created:
        like.delete()  # descurtir se já curtiu
    return redirect('new_post') 