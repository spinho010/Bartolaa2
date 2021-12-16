from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import AttConcluida, AttPendete, MetodoPag, NotaFiscal, Conclu_Serviço
# Register your models here.


class AdminattConclu(admin.ModelAdmin):
    list_display = ('dono_aparelho', 'modelo', 'concerto', 'valor', 'data_da_manutencao')

admin.site.register(AttConcluida, AdminattConclu)


class AdminattPende(admin.ModelAdmin):
        list_display = ('dono', 'modelo_aparelho', 'concerto_aparelho', 'valor_aparelho', 'data_entrega_aparelho')

admin.site.register(AttPendete, AdminattPende)


class AdminaNF(admin.ModelAdmin):
        list_display = ('nf_fiscal', 'valor_pago', 'data_venda', 'hora_venda', 'funcionario', 'metodo_pago')

admin.site.register(NotaFiscal, AdminaNF)


class AdminMPag(admin.ModelAdmin):
        list_display = ('mpagamento', 'descric')

admin.site.register(MetodoPag, AdminMPag)


class AdminSConclu(admin.ModelAdmin):
        list_display = ('serviço_concluido', 'descric')

admin.site.register(Conclu_Serviço, AdminSConclu)