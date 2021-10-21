from django.urls import path

from projeto.core import views as v
from .views import ListLista, CreateLista

app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
    path('lista-produtos/', ListLista.as_view(), name='listlista'),
    path('add-produtos/', CreateLista.as_view(), name='createlista'),
]
