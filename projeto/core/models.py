from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True


class ListaProdutos(models.Model):
    nome_produto = models.CharField(verbose_name='Nome do Produto: ', null=True, blank=True, max_length=100)
    descricao_produto = models.CharField(verbose_name='Descrição do Produto: ', null=True, blank=True, max_length=100)
    marca_produto = models.CharField(verbose_name='Marca do Produto: ', null=True, blank=True, max_length=100)
    custo_produto = models.CharField(verbose_name='Custo do Produto: ', null=True, blank=True, max_length=100)
    preço_produto = models.CharField(verbose_name='Preço do Produto: ', null=True, blank=True, max_length=100)
