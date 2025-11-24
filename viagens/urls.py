from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pacote/<int:pacote_id>/', views.detalhes, name='detalhes'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('adicionar/<int:pacote_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('remover/<int:pacote_id>/', views.remover_carrinho, name='remover_carrinho'),
    path('meu-carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('contato/', views.contato, name='contato'),
]
