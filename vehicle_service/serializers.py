from rest_framework import serializers
from .models import vehicle_details, fuel_types, vehicle_types, emission_nom
 
 
class fuel_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = fuel_types
        fields = '__all__'
 
class vehicle_types_serializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle_types
        fields = '__all__'
 
class emission_nom_serializer(serializers.ModelSerializer):
    class Meta:
        model = emission_nom
        fields = '__all__'

class vehicle_details_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = vehicle_details
        fields = '__all__'

class vehicle_details_serializers_by_daterange(serializers.ModelSerializer):

    class Meta:
        model =vehicle_details
        fields =('vin_no','registration_no','address','user_id','model_name','engine_no','created_at')
 
class vehicle_details_serializers_by_daterange_UTC(serializers.ModelSerializer):

    class Meta:
        model =vehicle_details
        fields =('vin_no','registration_no','address','user_id','model_name','engine_no','created_at')