from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(User):
    cpf = models.IntegerField()
    rg = models.CharField(max_length=40)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.first_name + " " + self.last_name

class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    imagem = models.ImageField()
    qtd_estoque = models.IntegerField()
    preco = models.FloatField()

    def __str__(self):
        return self.descricao

class Compras(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)