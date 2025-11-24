from django.db import models
from datetime import date

class Pacote(models.Model):

    CATEGORIAS = [
        ('NAC', 'Nacional'),
        ('INT', 'Internacional'),
    ]

    nome = models.CharField(max_length=200, verbose_name="Nome do Pacote")
    descricao = models.TextField(verbose_name="Descrição Completa")

    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")

    data_viagem = models.DateField(verbose_name="Data da Viagem")
    
    imagem = models.ImageField(upload_to='pacotes/', verbose_name="Foto do Destino")

    categoria = models.CharField(max_length=3, choices=CATEGORIAS, default='NAC')
    
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Pacotes de Viagem"


class Contato(models.Model):
    """Modelo para armazenar mensagens de contato de usuários."""
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    pacote = models.ForeignKey(Pacote, on_delete=models.SET_NULL, null=True, blank=True, help_text="Opcional: pacote ao qual a mensagem se refere")
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contato de {self.nome} - {self.email}"

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"