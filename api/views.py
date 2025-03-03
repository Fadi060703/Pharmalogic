from rest_framework import status 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView 
from .models import * 
from .serializers import * 
# Create your views here.


class LCPSOPV( APIView ) :
    serializer_class = PharamcyStorageOfProductsSerializer 
    def get( self , request : Request ) :
        list_of_prod = PharmacyStorageOfProducts.objects.all() 
        serializer = self.serializer_class( list_of_prod , many = True ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 
    def post( self , request : Request ) :
        rec_list = request.data 
        serializer = self.serializer_class( data = rec_list ) 
        if serializer.is_valid() :
            serializer.save()
            return Response( status = status.HTTP_201_CREATED ) 
        return Response( status = status.HTTP_400_BAD_REQUEST ) 


