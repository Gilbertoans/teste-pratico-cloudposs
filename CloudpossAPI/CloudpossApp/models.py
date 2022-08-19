from django.db import models

# Create your models here.
class Cliente(models.Model):
    ClienteId = models.AutoField(primary_key=True)
    ClienteNome = models.CharField(max_length=500)
    ClienteEmail = models.EmailField(max_length=500)
    ClienteTelefone = models.CharField(max_length=500)
    ClienteEndereco = models.CharField(max_length=500)
    ClienteProfissao = models.CharField(max_length=500)
    ClinteCurriculo = models.CharField(max_length=500)

 