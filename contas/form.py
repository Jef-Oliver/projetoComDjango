from django.forms import ModelForm
from .models import Transacao


class TransacaoForm(ModelForm):
    class Meta:  # mostrar fields que quero que aparecam na tela
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']
