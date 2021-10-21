from django.contrib import admin
from .models import ListaProdutos
from django.contrib.auth import admin as auth_admin
# Register your models here.

class ListaProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'descricao_produto', 'marca_produto', 'custo_produto', 'preço_produto')

admin.site.register(ListaProdutos, ListaProdutosAdmin)