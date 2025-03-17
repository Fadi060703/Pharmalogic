from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register( LocatedCity ) 
admin.site.register( ManufacturingLaboratory ) 
admin.site.register( ProductClassification ) 
admin.site.register( ProductConstraint ) 
admin.site.register( ProductType ) 
admin.site.register( Product ) 
admin.site.register( Pharmacy ) 
admin.site.register( PharmacyStorageOfProducts ) 
admin.site.register( InvoiceItem ) 
admin.site.register( Invoice )   
