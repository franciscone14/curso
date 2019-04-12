from django.shortcuts import render
from .models import Produto, Cliente
from .forms import (
    ClienteForm
)

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    produtos = Produto.objects.all()
    context = {
        "produtos": produtos
    }
    return render(request, 'core/index.html', context=context)

def nova_conta(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClienteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # try:
            cliente = Cliente()
            cliente.first_name = form.cleaned_data['first_name']
            cliente.last_name = form.cleaned_data['last_name']
            cliente.username = form.cleaned_data['username']
            cliente.email = form.cleaned_data['email']
            cliente.set_password(form.cleaned_data['password'])
            cliente.cpf = form.cleaned_data['cpf']
            cliente.rg = form.cleaned_data['rg']
            cliente.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'core/novo_cliente.html', {'message': "Deu certo :)"})
            # except Exception as e:
            #     form = ClienteForm()
            #     return render(request, 'core/novo_cliente.html', {
            #         'message': "Deu ruim :(",
            #         'form': form
            #     })
    else:
        form = ClienteForm()
    return render(request, 'core/novo_cliente.html', {'form': form})