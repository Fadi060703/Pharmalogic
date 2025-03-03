from .models import * 
from rest_framework import serializers 

class PharamcyStorageOfProductsSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = PharmacyStorageOfProducts 
        fields = '__all__' 