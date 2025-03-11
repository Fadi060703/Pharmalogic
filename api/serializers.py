from .models import * 
from django.contrib.auth.models import User 
from rest_framework import serializers 

class UserSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = User 
        fields = [ 'username' , 'first_name' , 'last_name' , 'email' ] 

class LocatedCitySerializer( serializers.ModelSerializer ) :
    class Meta :
        model = LocatedCity 
        fields = [ 'name' ] 

class ManufacturingLaboratorySerializer( serializers.ModelSerializer ) :
    location = LocatedCitySerializer( read_only = True ) 
    class Meta :
        model = ManufacturingLaboratory 
        fields = [ 'name' , 'location' , 'active' ]
        
class ProductClassificationSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = ProductClassification 
        fields = [ 'classification' ] 
        
class ProductConstraintSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = ProductConstraint 
        fields = [ 'constraint' ] 
        
class ProductTypeSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = ProductType 
        fields = [ 'type' ] 
        
class ProductSerializer( serializers.ModelSerializer ) :
    manufacturer = ManufacturingLaboratorySerializer( read_only = True )
    classification = ProductClassification( read_only = True ) 
    type = ProductTypeSerializer( read_only = True ) 
    constraints = ProductConstraintSerializer()
    class Meta :
        fields = [ 'name' , 'manufacturer' , 'classification' ,
                  'type' , 'description' , 'constraints' , 'needs_perscription' ] 
        
class PharmacySerializer( serializers.ModelSerializer ) :
    owner = UserSerializer( read_only = True )  
    located_city = LocatedCitySerializer( read_only = True )
    class Meta :
        model = Pharmacy 
        fields = [ 'owner' , 'name' , 'located_city' , 'address' ] 
        
 
                
