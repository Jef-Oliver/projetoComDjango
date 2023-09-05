from django.db import models


# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    observacoes = models.TextField(null=True, blank=True)
    # O ForeignKey quer dizer que a categoria é uma chave estrangeira e que uma transação só pode ter uma categoria
    # Mas que a categoria pode ter várias transações
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Transações'

    # O __str__ é o método que vai ser chamado quando o objeto for convertido para string
    def __str__(self):
        return self.descricao
