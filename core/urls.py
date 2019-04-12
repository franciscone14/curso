from django.urls import path
from .views import (
    index,
    nova_conta
)

urlpatterns = [
    path('', index),
    path('novo/cliente/', nova_conta, name="novo-cliente"),
]