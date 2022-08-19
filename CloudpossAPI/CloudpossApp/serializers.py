from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from CloudpossApp.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model=Cliente
    fields=('ClienteId','ClienteNome','ClienteEmail','ClienteTelefone','ClienteEndereco','ClienteProfissao','ClinteCurriculo')