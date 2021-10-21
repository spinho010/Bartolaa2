from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import ListaProdutos

def index(request):
    return render(request, 'index.html')


class ListLista(ListView):
    model = ListaProdutos
    template_name = 'listaproducts.html'


class CreateLista(CreateView):
    model = ListaProdutos
    fields = ['nome_produto', 'descricao_produto', 'marca_produto', 'custo_produto', 'preço_produto']
    template_name = 'createproducts.html'
    success_url = ('/')