from django import forms
from .models import Contato, Pacote


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'pacote', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@exemplo.com'}),
            'pacote': forms.Select(attrs={'class': 'form-select'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Escreva sua dúvida ou solicitação aqui...'}),
        }
        labels = {
            'nome': 'Nome',
            'email': 'E-mail',
            'pacote': 'Pacote (opcional)',
            'mensagem': 'Mensagem',
        }
