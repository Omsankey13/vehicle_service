"""
URL configuration for vehicle_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import view
 
urlpatterns = [
    #urls for vehicle details 
    path('api/vehicle/create-new-vehicle/', view.create_vehicle, name='create_vehicle'),
    path('api/vehicle/pk=<int:pk>', view.read_vehicle, name='read_vehicle'),
    path('api/vehicle/<int:pk>/update-exiting-vehicle/', view.update_vehicle, name='update_vehicle'),
    path('api/vehicle/<int:pk>/delete/', view.delete_vehicle, name='delete_vehicle'),
    path('api/vehicle/get_all_vehicle_list', view.get_all_vehicle_list, name='get_all_vehicle_list'),


    # URLs for fuel types
    path('api/fuel-type/create_fuel/', view.create_fuel, name='create_fuel_type'),
    path('api/fuel-type/get_all_fuel_list/', view.get_all_fuel_list, name='get_all_fuel_list'),
    path('api/fuel-type/<int:pk>/', view.read_fuel, name='read_fuel'),
    path('api/fuel-type/<int:pk>/update_fuel/', view.update_fuel, name='update_fuel'),
    path('api/fuel-type/<int:pk>/delete_fuel/', view.delete_fuel, name='delete_fuel'),
   
    # URLs for vehicle types
    path('api/vehicle-type/create/', view.create_vehicle_type, name='create_vehicle_type'),
    path('api/vehicle-type/get_all_vehicle_type_list',view.get_all_vehicle_type_list,name='get_all_vehicle_type_list'),
    path('api/vehicle-type/<int:pk>/', view.read_vehicle_type, name='read_vehicle_type'),
    path('api/vehicle-type/<int:pk>/update/', view.update_vehicle_type, name='update_vehicle_type'),
    path('api/vehicle-type/<int:pk>/delete/', view.delete_vehicle_type, name='delete_vehicle_type'),
   
    # URLs for emission nominal
    path('api/emission-nom/create/', view.create_emission_nom, name='create_emission_nom'),
    path('api/vehicle-type/get_all_ENOM_list',view.get_all_ENOM_list,name='get_all_ENOM_list'),
    path('api/emission-nom/<int:pk>/', view.read_emission_nom, name='read_emission_nom'),
    path('api/emission-nom/<int:pk>/update/', view.update_emission_nom, name='update_emission_nom'),
    path('api/emission-nom/<int:pk>/delete/', view.delete_emission_nom, name='delete_emission_nom'),


    #interservice-call
    # path('api/get_vehicle_details_by_UTC_date_range',view.get_vehicle_details_by_UTC_date_range,name='get_vehicle_details_by_UTC_date_range'),
    path('api/get_vehicle_details_by_id',view.get_vehicle_details_by_id,name='get_vehicle_details_by_id'),
    path('api/get_vehicle_details_by_date',view.get_vehicle_details_by_date_range,name='get_vehicle_details_by_date'),
    path('api/vehicle_details/get_vehicle_details_utc',view.get_vehicle_details_utc,name='get_vehicle_details_utc')
]
 