from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import AttConcluida, AttPendete, MetodoPag, NotaFiscal, Conclu_Serviço, AguardandoRetirada, entrada_saida_att, mensal_diario, positivo_negativo, relatorio_mensal, relatorios
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


class AdminAguardando(admin.ModelAdmin):
        list_display = ('name_cliente', 'm_aparelho', 'Falta_Pagar', 'f_pagar_valor')

admin.site.register(AguardandoRetirada, AdminAguardando)


class entrada_saida_attAdmin(admin.ModelAdmin):
        list_display = ('entrada_ou_saida', 'descric')

admin.site.register(entrada_saida_att, entrada_saida_attAdmin)


class mensal_diario_Admin(admin.ModelAdmin):
        list_display = ('mensal_diario', 'descric')

admin.site.register(mensal_diario, mensal_diario_Admin)


class positivo_negativoAdmin(admin.ModelAdmin):
        list_display = ('positiv_negativo', 'descric')

admin.site.register(positivo_negativo, positivo_negativoAdmin)


class relatoriosAdmin(admin.ModelAdmin):
        list_display = ('compra_ou_venda', 'valor_r', 'motivo', 'data_r')

admin.site.register(relatorios, relatoriosAdmin)


class relatorio_mensalAdmin(admin.ModelAdmin):
        list_display = ('d_ou_m', 'p_ou_n', 'total', 'mes_relatorio', 'data_rm')

admin.site.register(relatorio_mensal, relatorio_mensalAdmin)