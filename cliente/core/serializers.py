from cliente.core.models import Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome','data_registro','contatos']
        # fields = '__all__'
