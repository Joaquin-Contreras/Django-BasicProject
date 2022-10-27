from ast import Not
from lib2to3.pgen2.token import EQEQUAL
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Topico
from .forms import PostForm
from datetime import date

# Create your views here.


def Posts(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    temas = Topico.objects.all()
    postMios = Post.objects.filter(user=request.user).order_by('fecha')
    posts = Post.objects.exclude(user=request.user).filter(topico__tema__icontains= q)
    return render(request, 'posts.html', {
        'posts': posts,
        'postMios': postMios,
        'temas': temas,
    })


def PostDetalle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'post_detalle.html', {
        'post': post
    })


@login_required
def crearPost(request):
    if request.method == 'GET':
        return render(request, 'crearPost.html', {
            'form': PostForm
        })
    try:
        form = PostForm(request.POST)
        nuevoPost = form.save(commit=False)
        nuevoPost.user = request.user
        nuevoPost.fecha = date.today()
        nuevoPost.save()
        return redirect('/blog')
    except ValueError:
        return render(request, 'crearPost.html', {
            'form': PostForm,
            'error': "ERROR",
        })