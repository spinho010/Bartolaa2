from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

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

class MetodoPag(models.Model):
    mpagamento = models.CharField(verbose_name='Metodo de Pagamento:', max_length=60, blank=True)
    descric = models.CharField(verbose_name='Descrição:', max_length=60, blank=True)

    def __str__(self):
        return "{}".format(self.mpagamento)


class Conclu_Serviço(models.Model):
    serviço_concluido = models.CharField(verbose_name='Serviço Concluido?: ', max_length=60, blank=True)
    descric = models.CharField(verbose_name='Descrição:', max_length=60, blank=True)

    def __str__(self):
        return "{}".format(self.serviço_concluido)


class AttPendete(models.Model):
    dono = models.CharField(verbose_name='Dono do aparelho:', max_length=60, blank=True)
    modelo_aparelho = models.CharField(verbose_name='Modelo do aparelho:', max_length=60, blank=True)
    concerto_aparelho = models.CharField(verbose_name='Problema do aparelho:', max_length=600, blank=True)
    valor_aparelho = models.CharField(verbose_name='Valor do Concerto:', max_length=60, blank=True)
    data_entrega_aparelho = models.CharField(verbose_name='Data para entregar:', max_length=60, blank=True)
    finalizado = models.ForeignKey(Conclu_Serviço, max_length=100, null=True, on_delete=models.PROTECT)



class AttConcluida(models.Model):
    dono_aparelho = models.CharField(verbose_name='Dono do aparelho:', max_length=60, blank=True)
    modelo = models.CharField(verbose_name='Modelo do aparelho:', max_length=60, blank=True)
    concerto = models.CharField(verbose_name='Problema do aparelho:', max_length=600, blank=True)
    valor = models.CharField(verbose_name='Valor do Concerto:', max_length=60, blank=True)
    data_da_manutencao = models.CharField(verbose_name='Data entregue:', max_length=60, blank=True)


class NotaFiscal(models.Model):
    n_cliente = models.CharField(verbose_name='Nome do Cliente:', max_length=60, blank=True)
    nf_fiscal = models.CharField(verbose_name='Codigo Fiscal:', max_length=60, blank=True)
    valor_pago = models.CharField(verbose_name='Valor Pago:', max_length=60, blank=True)
    data_venda = models.CharField(verbose_name='Data da Venda:', max_length=60, blank=True)
    hora_venda = models.CharField(verbose_name='Data da Venda:', max_length=60, blank=True)
    funcionario = models.CharField(verbose_name='Funcionário:', max_length=60, blank=True)
    metodo_pago = models.ForeignKey(MetodoPag, max_length=100, null=True, on_delete=models.PROTECT)


class AguardandoRetirada(models.Model):
    name_cliente = models.CharField(verbose_name='Nome ', max_length=60, null=False)
    m_aparelho = models.CharField(verbose_name='Modelo Do Aparelho ', max_length=60, null=False)
    Falta_Pagar = models.ForeignKey(Conclu_Serviço, max_length=100, null=False, on_delete=models.PROTECT)
    f_pagar_valor = models.CharField(verbose_name='Valor a Pagar: ', max_length=60, blank=True, null=True)


    def __str__(self):
        return "{}".format(self.m_aparelho)