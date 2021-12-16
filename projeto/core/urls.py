from django.urls import path

from projeto.core import views as v
from .views import TempAtividade, TempAtividadeCon, TempAtividadePen, NF_Fiscaal, CreateConclu

app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
    path('atividades/', TempAtividade.as_view(), name='ativv'),
    path('atividades/pendentes', TempAtividadePen.as_view(), name='ativvp'),
    path('atividades/concluidas', TempAtividadeCon.as_view(), name='ativvc'),
    path('nota_fiscal/', NF_Fiscaal.as_view(), name='nf'),
    path('create_attc/', CreateConclu.as_view(), name='create-concluida'),
]
