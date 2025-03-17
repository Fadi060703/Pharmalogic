from django.urls import path 
from .views import * 
urlpatterns = [
    #Located Cities 
    path( 'cities' , ListCreateLocatedCityView.as_view() , name = 'cities' ) ,
    path( 'cities/<int:pk>' , LocatedCityDetailView.as_view() , name = 'city-detail' ) ,
    #Laboratories 
    path( 'labs' , ListCreateManufacturingLaboratoryView.as_view() , name = 'labs' ) ,
    path( 'labs/<int:pk>' , ManufacturingLaboratoryDetailView.as_view() , name ='lab-detail' ) ,
]
