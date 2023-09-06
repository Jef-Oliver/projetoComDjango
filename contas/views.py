from django.shortcuts import render, redirect

from .form import TransacaoForm
from .models import Transacao


def home(request):
    data = {}
    return render(request, "contas/home.html", data)


def listagem(request):
    data = {'transacoes': Transacao.objects.all()}
    return render(request, "contas/listagem.html", data)


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)  # se não tiver nada no request.POST, ele vai criar um formulário vazio

    # Verificar se o form é válido
    if form.is_valid():
        form.save()
        return redirect('url_listagem')  # ao salvar o formulário, redireciona para a página de listagem

    return render(request, "contas/form.html", {'form': form})


def update(request, pk):  # pk é a chave primária do objeto que queremos atualizar
    # pegar transação do banco de dados
    transacao = Transacao.objects.get(pk=pk)
    # instanciando form
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render(request, "contas/form.html", {'form': form, 'transacao': transacao})


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk) # Recupero a transação do banco de dados
    transacao.delete() # Deleto a transação
    return redirect('url_listagem') # Redireciono para a página de listagem