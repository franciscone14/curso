from django import forms
from django.contrib.auth.models import (User)
from .models import (
    Cliente
)

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'password',
            'username',
            'first_name',
            'last_name',
            'email',
            'cpf',
            'rg'
        ]