""" Tabelas do banco de dados """
from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    """ Cadastro de clientes """
    nome = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    id_sessao = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)


class Categoria (models.Model):
    """ Categorias (Masculino, Feminino, Infantil, etc) """
    nome = models.CharField(max_length=255, null=True, blank=True)


class Tipo (models.Model):
    """ Tipos (Camisa, Camiseta, Bermuda, Calça, etc) """
    nome = models.CharField(max_length=255, null=True, blank=True)


class Produto (models.Model):
    """ Cadastro de produtos """
    imagem = models.CharField(max_length=255, null=True, blank=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(
        Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    tipo = models.ForeignKey(
        Tipo, null=True, blank=True, on_delete=models.SET_NULL)


class ItemEstoque (models.Model):
    """ Quantidade e tipo de item no estoque """
    produto = models.ForeignKey(
        Produto, null=True, blank=True, on_delete=models.SET_NULL)
    cor = models.CharField(max_length=255, null=True, blank=True)
    tamanho = models.CharField(max_length=255, null=True, blank=True)
    quantidade = models.IntegerField(default=0)


class Endereco (models.Model):
    """ Endereço do cliente """
    rua = models.CharField(max_length=255, null=True, blank=True)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    cep = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)
    cliente = models.ForeignKey(
        Cliente, null=True, blank=True, on_delete=models.SET_NULL)


class Pedido (models.Model):
    """ Pedido do cliente """
    cliente = models.ForeignKey(
        Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    finalizado = models.BooleanField(default=False)
    codigo_transacao = models.CharField(max_length=255, null=True, blank=True)
    endereco = models.ForeignKey(
        Endereco, null=True, blank=True, on_delete=models.SET_NULL)
    data_finalizacao = models.DateTimeField(null=True, blank=True)


class ItensPedido (models.Model):
    """ Item do pedido """
    itemestoque = models.ForeignKey(
        ItemEstoque, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)
    pedido = models.ForeignKey(
        Pedido, null=True, blank=True, on_delete=models.SET_NULL)
