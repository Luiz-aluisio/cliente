from cliente.core.models import Cliente
from rest_framework import permissions, viewsets
from cliente.core.serializers import ClienteSerializer
from cliente.core.models import Cliente


class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint to Cliente
    """
    queryset = Cliente.objects.all().order_by('nome')
    serializer_class = ClienteSerializer
    # permission_classes = [permissions.IsAuthenticated]
