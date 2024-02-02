from cliente.core.models import Cliente, Contato
from rest_framework import serializers

class ContatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contato
        fields = ['id', 'telefone', 'email', 'url', 'cliente']


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    contatos = ContatoSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'data_registro', 'contatos', 'url']
        # fields = '__all__'
