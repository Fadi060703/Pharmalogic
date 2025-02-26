from django.db import models

class LocatedCity( models.Model ) :
    name = models.CharField( max_length = 20 ) 
    def __str__( self ) :
        return self.name  

class ManufacturingLabratory( models.Model ) :
    name = models.CharField( max_length = 255 ) 
    location = models.ForeignKey( LocatedCity , on_delete = models.CASCADE , related_name = 'Lab-Location' ) 
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
    manufacturer = models.ForeignKey( ManufacturingLabratory , on_delete = models.CASCADE , related_name = 'Product-Manuacturer' )
    classification = models.ForeignKey( ProductClassification , on_delete = models.CASCADE , related_name = 'Product-Class' )
    productType = models.ForeignKey( ProductType , on_delete = models.CASCADE , related_name = 'Product-Type' )  
    description = models.TextField() 
    constraints = models.ManyToManyField( ProductConstraint , related_name = 'Product-Constraints' ) 
    needs_perscription = models.BooleanField( default = False ) 
    
    

    
    