from rest_framework import viewsets, status
from .serializers import PdfSerializer
from .models import Crudpdf
from handlers.response import custom_response

# Create your views here.
#En una app maximo de 4 APIS
class UserViewSet(viewsets.ViewSet):
  #GET
  def list(self, request):
    query = Crudpdf.objects.all()
    serializer = PdfSerializer(query, many=True)
    return custom_response("Lista de todos los archivos", serializer.data, False, status.HTTP_200_OK)

  #POST
  def create(self, request):
    data = request.data
    serializer = PdfSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return custom_response("Archivo cargado correctamente", serializer.data, False, status.HTTP_200_OK)
    else: 
      return custom_response("Error al cargar el archivo", serializer.errors, True, status.HTTP_400_BAD_REQUEST)

  #PUT
  def update(self, request, pk=None):
    try:
      query = Crudpdf.objects.get(id=pk)
    except Crudpdf.DoesNotExist:
      return custom_response("No se pudo actualizer el archivo correctamente", serializer.data, False, status.HTTP_400_BAD_REQUEST)

    data = request.data
    serializer = PdfSerializer(instance = query, data = data)
    if serializer.is_valid():
      serializer.save()
      return custom_response("Archivo actualizado correctamentee", serializer.data, False, status.HTTP_200_OK)
    else:
      return custom_response("No se pudo actualizar el archivo correctamente", serializer.data, False, status.HTTP_400_BAD_REQUEST)

  #DELETE
  def delete(self, request, pk=None):
    try:
      query = Crudpdf.objects.get(id=pk)
    except Crudpdf.DoesNotExist:
      return custom_response("Se elimino el archivo correctamente", None, False, status.HTTP_400_BAD_REQUEST)
    
    query.delete()
    return custom_response("El archivo se elimino correctamente", None, False, status.HTTP_200_OK)
    