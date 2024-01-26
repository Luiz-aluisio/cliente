from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    telefone = models.CharField(max_length=11)
    email = models.EmailField(null=True, blank=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='contatos')

    def __str__(self):
        return self.telefone
    


