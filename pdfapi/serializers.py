#Importacion de los serializers
from rest_framework import serializers 
from .models import Crudpdf

class PdfSerializer(serializers.ModelSerializer):
  class Meta:
    model = Crudpdf 
    fields = '__all__'
