from multiprocessing.connection import Client
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from CloudpossApp.serializers import ClienteSerializer

from CloudpossApp.models import Cliente
from django.core.files.storage import default_storage
# Create your views here.

@csrf_exempt
def CloudpossAPI(request,id=0): 
  global Cliente 
  if request.GET:
    Cliente = Cliente.objects.all
    cliente_serializer = ClienteSerializer(Cliente,many=True)
    return JsonResponse(cliente_serializer.data,safe=False)
  elif request.method=='POST':
    cliente_data=JSONParser().parse(request)
    cliente_Serializer=ClienteSerializer(data=cliente_data)
    if cliente_Serializer.is_valid():
        Cliente_Serializer.save()
        return JsonResponse("Cliente adicionado com sucesso",safe=False)
    return JsonResponse("Falha ao salvar cliente",safe=False)   
  elif request.method=='PUT':
    Cliente_data=JSONParser().parse(request)
    Cliente=Cliente.objects.get(ClienteId=Cliente_data['ClienteId'])
    Cliente_Serializer=ClienteSerializer(Cliente,data=Cliente_data)
    if Cliente_Serializer.is_valid():
      Cliente_Serializer.save()
      return JsonResponse("Atualizado com sucesso",safe=False)
    return JsonResponse("Falha ao atualizar")
  elif request.method=='DELETE':
    Cliente=Cliente.objects.get(ClienteId=id)
    Cliente.delete()
    return JsonResponse("Cliente deletado",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)