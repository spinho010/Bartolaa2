from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import AttConcluida, AttPendete, NotaFiscal


def index(request):
    return render(request, 'index.html')


class TempAtividade(TemplateView):
    template_name = 'atividades.html'


class TempAtividadePen(ListView):
    model = AttPendete
    template_name = 'atividades-pendente.html'


class AtividadeDelete(UpdateView):
    model = AttPendete
    fields = ['data_entrega_aparelho', 'finalizado']
    template_name = 'attpendente-delete.html'
    success_url = ('/')


class TempAtividadeCon(ListView):
    model = AttConcluida
    template_name = 'atividades-concluida.html'


class NF_Fiscaal(ListView):
    model = NotaFiscal
    template_name = 'nf-fiscal.html'


class CreateConclu(CreateView):
    model = AttConcluida
    fields = ['dono_aparelho', 'modelo', 'concerto', 'valor', 'data_da_manutencao']
    template_name = 'attconcluidis.html'
    success_url = ('/')


class CreatePende(CreateView):
    model = AttPendete
    fields = ['dono', 'modelo_aparelho', 'concerto_aparelho', 'valor_aparelho', 'data_entrega_aparelho']
    template_name = 'attconcluidis.html'
    success_url = ('/')




