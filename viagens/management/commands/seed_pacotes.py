from django.core.management.base import BaseCommand
from decimal import Decimal
from datetime import date

from viagens.models import Pacote


class Command(BaseCommand):
    help = 'Insere dois pacotes de exemplo: Disney e Cruzeiro dos Solteiros'

    def handle(self, *args, **options):
        pacotes = [
            {
                'nome': 'Disney - 3 Dias Básico (1 Parque Tematico por dia)',
                'descricao': 'Disney - 3 Dias Básico (1 Parque Tematico por dia)\nTarifa reembolsável\n1 adulto',
                'preco': Decimal('3249.93'),
                'data_viagem': date(2026, 1, 8),
                'imagem': 'pacotes/disney.jpeg',
                'categoria': 'INT',
                'ativo': True,
            },
            {
                'nome': 'Cruzeiro dos Solteiros - 3 Dias Básico',
                'descricao': 'Cruzeiro dos Solteiros - 3 Dias Básico\nTarifa reembolsável\n1 adulto',
                'preco': Decimal('10249.00'),
                'data_viagem': date(2026, 2, 15),
                'imagem': 'pacotes/Solteiros.jpg',
                'categoria': 'INT',
                'ativo': True,
            },
        ]

        for item in pacotes:
            obj, created = Pacote.objects.get_or_create(
                nome=item['nome'],
                defaults={
                    'descricao': item['descricao'],
                    'preco': item['preco'],
                    'data_viagem': item['data_viagem'],
                    'imagem': item['imagem'],
                    'categoria': item['categoria'],
                    'ativo': item['ativo'],
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Criado: {obj.nome}"))
            else:
                self.stdout.write(self.style.WARNING(f"Já existe: {obj.nome}"))

        self.stdout.write(self.style.SUCCESS('Operação concluída.'))
