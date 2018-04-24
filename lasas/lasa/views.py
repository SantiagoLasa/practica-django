# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *



# Create your views here.

def index(request):
    return render(request, "index.html")

def poste(request):
    posts = Post.objects.all()
    return render(request, "post.html", {'todos_los_post':posts})

def crear_post(request):
    if request.method == "POST":
        nuevo_titulo = request.POST["titulo"]
        nuevo_texto = request.POST["texto"]
        nuevo_post = Post(titulo=nuevo_titulo, texto=nuevo_texto)
        nuevo_post.save()
        return redirect('poste') 

def articulo(request, id_articulo):
    articulo = Post.objects.get(id=id_articulo)
    print articulo
    #Renderizar un Template que muestre los datos del articulo
    return render(request, "articulo.html", {'el_articulo':articulo})
