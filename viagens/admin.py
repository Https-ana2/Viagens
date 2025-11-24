from django.contrib import admin
from .models import Pacote
from .models import Contato

@admin.register(Pacote)
class PacoteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'data_viagem', 'ativo')
    list_filter = ('ativo', 'categoria')
    search_fields = ('nome', 'descricao')

# Register your models here.


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'pacote', 'criado_em')
    list_filter = ('criado_em',)
    search_fields = ('nome', 'email', 'mensagem')
