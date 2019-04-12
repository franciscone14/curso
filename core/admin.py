from django.contrib import admin
from .models import (Produto)

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'qtd_estoque', 'preco',]

admin.site.register(Produto, ProdutoAdmin)