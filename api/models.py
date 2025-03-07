from django.db import models
from django.contrib.auth.models import User
class LocatedCity( models.Model ) :
    name = models.CharField( max_length = 20 ) 
    def __str__( self ) :
        return self.name  

class ManufacturingLabratory( models.Model ) :
    name = models.CharField( max_length = 255 ) 
    location = models.ForeignKey( LocatedCity , on_delete = models.CASCADE , related_name = 'Lab_Location' ) 
    active = models.BooleanField( default = True ) 
    def __str__( self ) :
        return self.name

class ProductClassification( models.Model ) :
    classification = models.CharField( max_length = 50 ) 
    def __str__( self ) :
        return self.classification
    
class ProductConstraint( models.Model ) :
    constraint = models.CharField( max_length = 255 ) 
    def __str__( self ) :
        return self.constraint 
    
class ProductType( models.Model ) :
    type = models.CharField( max_length = 30 )
    def __str__( self ) :
        return self.type 
    
class Product( models.Model ) :
    name = models.CharField( max_length = 255 ) 
    manufacturer = models.ForeignKey( ManufacturingLabratory , on_delete = models.CASCADE , related_name = 'Product_Manuacturer' )
    classification = models.ForeignKey( ProductClassification , on_delete = models.CASCADE , related_name = 'Product_Class' )
    productType = models.ForeignKey( ProductType , on_delete = models.CASCADE , related_name = 'Product_Type' )  
    description = models.TextField() 
    constraints = models.ManyToManyField( ProductConstraint , related_name = 'Product_Constraints' ) 
    needs_perscription = models.BooleanField( default = False ) 
    def __str__( self ) :
        return self.name 
    
class Pharmacy( models.Model ) :
    owner = models.OneToOneField( User , related_name = 'pharmacy_owner' , on_delete = models.CASCADE ) 
    name = models.CharField( max_length = 200 )
    located_city = models.ForeignKey( LocatedCity , on_delete = models.CASCADE ) 
    address = models.TextField()
    def __str__( self ) :
        return self.name 

class PharmacyStorageOfProducts( models.Model ) :
    pharmacy = models.ForeignKey( Pharmacy , on_delete = models.CASCADE , related_name = 'pharmacy_storage' ) 
    products = models.ManyToManyField( Product , related_name = 'linking_products' ) 
    count = models.IntegerField( default = 0 )  
    
class Envoice( models.Model ) :
    pharmacy = models.ForeignKey( Pharmacy , on_delete = models.CASCADE , related_name = 'pharmacy_envoice' ) 
    products = models.ManyToManyField( Product , related_name = 'envoice_products' ) 
    count = models.IntegerField( default = 1 ) 
    date = models.DateTimeField( auto_now_add = True ) 
    is_checked = models.BooleanField( default = False )
        
    
    