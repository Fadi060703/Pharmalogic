from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator 
class LocatedCity( models.Model ) :
    name = models.CharField( max_length = 20 ) 
    def __str__( self ) :
        return f'{ self.name }'  

class ManufacturingLaboratory( models.Model ) :
    name = models.CharField( max_length = 255 ) 
    location = models.ForeignKey( LocatedCity , on_delete = models.CASCADE , related_name = 'Lab_Location' ) 
    active = models.BooleanField( default = True ) 
    def __str__( self ) :
        status = 'Active' if self.active else "Inactive" 
        return f'{ self.name } ({ self.location }) - { status }' 

class ProductClassification( models.Model ) :
    classification = models.CharField( max_length = 50 ) 
    def __str__( self ) :
        return f'{ self.classification }'
    
class ProductConstraint( models.Model ) :
    constraint = models.CharField( max_length = 255 ) 
    def __str__( self ) :
        return f'{ self.constraint }' 
    
class ProductType( models.Model ) :
    type = models.CharField( max_length = 30 )
    def __str__( self ) :
        return f'{ self.type }'
    
class Product( models.Model ) :
    name = models.CharField( max_length = 255 ) 
    manufacturer = models.ForeignKey( ManufacturingLaboratory , on_delete = models.CASCADE , related_name = 'Product_Manuacturer' )
    classification = models.ForeignKey( ProductClassification , on_delete = models.CASCADE , related_name = 'Product_Class' )
    productType = models.ForeignKey( ProductType , on_delete = models.CASCADE , related_name = 'Product_Type' )  
    description = models.TextField() 
    constraints = models.ManyToManyField( ProductConstraint , related_name = 'Product_Constraints' ) 
    needs_perscription = models.BooleanField( default = False ) 
    def __str__( self ) :
        return self.name 
    
class Pharmacy( models.Model ) :
    owner = models.OneToOneField( User , related_name = 'pharmacy_owner' , on_delete = models.CASCADE ) 
    name = models.CharField( max_length = 200 , unique = True )
    located_city = models.ForeignKey( LocatedCity , on_delete = models.CASCADE ) 
    address = models.TextField()
    def __str__( self ) :
        return self.name 

class PharmacyStorageOfProducts( models.Model ) :
    pharmacy = models.ForeignKey( Pharmacy , on_delete = models.CASCADE , related_name = 'pharmacy_storage' ) 
    product = models.ForeignKey( Product , related_name = 'linking_products' , on_delete = models.CASCADE ) 
    count = models.IntegerField( default = 0 , validators = [ MinValueValidator( 0 ) ] )  
    
class InvoiceItem( models.Model ) :
    item = models.ForeignKey( Product , on_delete = models.CASCADE , related_name = 'Items_Envoice' ) 
    price = models.DecimalField( max_digits = 20 , decimal_places = 2 )  
    count = models.IntegerField( default = 0 , validators = [ MinValueValidator( 1 ) ] )
           
class Invoice( models.Model ) :
    pharmacy = models.ForeignKey( Pharmacy , on_delete = models.CASCADE , related_name = 'pharmacy_envoice' ) 
    products = models.ManyToManyField( Product , through = 'InvoiceItem' , related_name = 'Products_Bought' )   
    date = models.DateTimeField( auto_now_add = True ) 
    is_checked = models.BooleanField( default = False )
        
    
    