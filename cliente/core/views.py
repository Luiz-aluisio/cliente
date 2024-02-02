from cliente.core.models import Cliente, Contato
from rest_framework import permissions, viewsets
from cliente.core.serializers import ClienteSerializer, ContatoSerializer
from cliente.core.models import Cliente


class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint to Cliente
    """
    queryset = Cliente.objects.all().order_by('nome')
    serializer_class = ClienteSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all().order_by('email')
    serializer_class = ContatoSerializer
