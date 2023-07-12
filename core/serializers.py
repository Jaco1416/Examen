from .models import *
from rest_framework import serializers


class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class TipoEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEstado
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    tipo = TipoProductoSerializer(read_only=True)
    class Meta:
        model = Producto
        fields = '__all__'

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'