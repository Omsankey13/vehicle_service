from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import vehicle_details,fuel_types,vehicle_types,emission_nom
from .serializers import vehicle_details_serializer,fuel_type_serializer,vehicle_types_serializer,emission_nom_serializer
import time
from functools import wraps
 
def measure_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

@csrf_exempt
@measure_execution_time
def create_vehicle(request):
    try:
        if request.method == "POST":
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request
           
            serializer = vehicle_details_serializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Vehicle created successfully!!", "data": serializer.data}, status=201)
            else:
                return JsonResponse({"message": "Invalid Data Provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid Http Method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    

@csrf_exempt
@measure_execution_time
def get_all_vehicle_list(request):
    try:
        vehicle_object = vehicle_details.objects.filter(is_deleted=False)
        serializer = vehicle_details_serializer(vehicle_object, many=True)
        if serializer.data:
            return JsonResponse({"message":"vehicle details retrieved successfully!!","total":len(serializer.data),"data":serializer.data})
        else:
            return JsonResponse({"message":"No data found!!"})
    except Exception as error:
        print("get_all_vehicle_list(): ", error)
        return JsonResponse({"message":"Something went wrong"},status=500)
 
@csrf_exempt
@measure_execution_time
def read_vehicle(request, pk):
    try:
        vehicle = vehicle_details.objects.get(pk=pk)
        print('None',vehicle)
        serializer = vehicle_details_serializer(vehicle)
        return JsonResponse({"message": "Vehicle details retrieved successfully!!", "data": serializer.data})

    except Exception as error:
        print('Read_vehicle():',error)
        return JsonResponse({"message": "Something went wrong"}, status=500)
 
@csrf_exempt
@measure_execution_time
def update_vehicle(request, pk):
    try:
        vehicle = vehicle_details.objects.get(pk=pk)
        if request.method == 'PUT':
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request
           
            serializer = vehicle_details_serializer(vehicle, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Vehicle updated successfully!!!", "data": serializer.data})
            else:
                return JsonResponse({"message": "Invalid data provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        print("update_vehicle(): ", error)
        return JsonResponse({"message": "Something went wrong"}, status=500)
 
@csrf_exempt
@measure_execution_time
def delete_vehicle(request, pk):
    try:
        vehicle = vehicle_details.objects.get(pk=pk)
        if request.method == 'DELETE':
            vehicle.delete()
            return JsonResponse({"message": "Vehicle deleted successfully!!!"})
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        print('delete_vehicle()',error)
        return JsonResponse({"message": "Something went wrong"}, status=500)
    
#Fuel Types CRUD

@csrf_exempt
@measure_execution_time
def create_fuel(request):
    try:
        if request.method == "POST":
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request
           
            serializer = fuel_type_serializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Fuel created successfully!!", "data": serializer.data}, status=201)
            else:
                return JsonResponse({"message": "Invalid Data Provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid Http Method"}, status=405)
    except Exception as error:
        print('Create_fuel() :',error)
        return JsonResponse({"message": "Something went wrong"}, status=500)
    
@csrf_exempt
@measure_execution_time
def get_all_fuel_list(request):
    try:
        fuel_object = fuel_types.filter(is_deleted=False)
        serializer = fuel_type_serializer(fuel_object, many=True)
        if serializer.data:
            return JsonResponse({"message":"Fuel types list retrieved successfully!!","total":len(serializer.data),"data":serializer.data})
        else:
            return JsonResponse({"message":"No data found!!"})
    except Exception as error:
        print("get_all_vehicle_list(): ", error)
        return JsonResponse({"message":"Something went wrong"},status=500)
    
@csrf_exempt
@measure_execution_time
def read_fuel(request, pk):
    try:
        fuel_object = fuel_types.objects.get(pk=pk,is_delete=False)
        serializer = fuel_type_serializer(fuel_object)
        return JsonResponse({"message": "Fuel types retrieved successfully!!", "data": serializer.data})

    except Exception as error:
        print('Read_fuel():',error)
        return JsonResponse({"message": "Something went wrong"}, status=500)
 
@csrf_exempt
@measure_execution_time
def update_fuel(request, pk):
    try:
        fuel = fuel_types.get(pk=pk)
        if request.method == 'PUT':
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request
           
            serializer = fuel_type_serializer(fuel, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Fuel Types updated successfully!!!", "data": serializer.data})
            else:
                return JsonResponse({"message": "Invalid data provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        print("update_vehicle(): ", error)
        return JsonResponse({"message": "Something went wrong"}, status=500)
 
@csrf_exempt
@measure_execution_time
def delete_fuel(request, pk):
    try:
        fuel = fuel_types.objects.get(pk=pk)
        if request.method == 'DELETE':
            fuel.delete()
            return JsonResponse({"message":"fuel deleted successfully!!!"})
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        print('delete_vehicle()',error)
        return JsonResponse({"message": "Something went wrong"}, status=500)
    

#Vehicle types CRUD operation
from rest_framework.decorators import api_view
@api_view(['POST'])
@csrf_exempt
@measure_execution_time
def create_vehicle_type(request):
    try:
    
        if type(request) != dict:
            request_data = json.loads(request.body)
        else:
            request_data = request

        serializer = vehicle_types_serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Vehicle type created successfully!!", "data": serializer.data},
                                status=201)
        else:
            return JsonResponse({"message": "Invalid Data Provided", "errors": serializer.errors}, status=400)
        
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    
@csrf_exempt
@measure_execution_time
def get_all_vehicle_type_list(request):
    try:
        vehicle_object = vehicle_types.filter(is_deleted=False)
        serializer = vehicle_types_serializer(vehicle_object, many=True)
        if serializer.data:
            return JsonResponse({"message":"all vehicle types list retrieved successfully!!","total":len(serializer.data),"data":serializer.data})
        else:
            return JsonResponse({"message":"No data found!!"})
    except Exception as error:
        print("get_all_vehicle_type_list(): ", error)
        return JsonResponse({"message":"Something went wrong"},status=500)
 
 
@csrf_exempt
@measure_execution_time
def read_vehicle_type(request, pk):
    try:
        vehicle_type = vehicle_types.objects.get(pk=pk)
        serializer = vehicle_types_serializer(vehicle_type)
        return JsonResponse({"message": "Vehicle type details retrieved successfully!!", "data": serializer.data})
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
 
 
@csrf_exempt
@measure_execution_time
def update_vehicle_type(request, pk):
    try:
        vehicle_type = vehicle_types.objects.get(pk=pk)
        if request.method == 'PUT':
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request
 
            serializer = vehicle_types_serializer(vehicle_type, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Vehicle type updated successfully!!!", "data": serializer.data})
            else:
                return JsonResponse({"message": "Invalid data provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
 
 
@csrf_exempt
@measure_execution_time
def delete_vehicle_type(request, pk):
    try:
        vehicle_type = vehicle_types.objects.get(pk=pk)
        if request.method == 'DELETE':
            vehicle_type.delete()
            return JsonResponse({"message": "Vehicle type deleted successfully!!!"})
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    
#Emission nom  CRUD Operation
    
@csrf_exempt
@measure_execution_time
def create_emission_nom(request):
    try:
        if request.method == "POST":
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request
 
            serializer = emission_nom_serializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Emission nominal created successfully!!", "data": serializer.data},
                                    status=201)
            else:
                return JsonResponse({"message": "Invalid Data Provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid Http Method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    
@csrf_exempt
@measure_execution_time
def get_all_ENOM_list(request):
    try:
        ENOM_object = emission_nom.filter(is_deleted=False)
        serializer = emission_nom_serializer(ENOM_object, many=True)
        if serializer.data:
            return JsonResponse({"message":" ENOM list retrieved successfully!!","total":len(serializer.data),"data":serializer.data})
        else:
            return JsonResponse({"message":"No data found!!"})
    except Exception as error:
        print("get_all_vehicle_list(): ", error)
        return JsonResponse({"message":"Something went wrong"},status=500)
 
 
@csrf_exempt
@measure_execution_time
def read_emission_nom(request, pk):
    try:
        emission_nominal = emission_nom.objects.get(pk=pk)
        serializer = emission_nom_serializer(emission_nominal)
        return JsonResponse({"message": "Emission nominal details retrieved successfully!!", "data": serializer.data})
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
   
@csrf_exempt
@measure_execution_time
def update_emission_nom(request, pk):
    try:
        emission_nom = emission_nom.objects.get(pk=pk)
        if request.method == 'PUT':
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request
 
            serializer = emission_nom_serializer(emission_nom, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Emission Nom updated successfully!!!", "data": serializer.data})
            else:
                return JsonResponse({"message": "Invalid data provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
 
@csrf_exempt
@measure_execution_time
def delete_emission_nom(request, pk):
    try:
        emission_nom = emission_nom.objects.get(pk=pk)
        if request.method == 'DELETE':
            emission_nom.delete()
            return JsonResponse({"message": "Emission Nom deleted successfully!!!"})
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    

#Inter service call by using date 
from rest_framework.decorators import api_view

@api_view(['GET'])
@csrf_exempt
def get_vehicle_details_by_id(request):
    try:
        user_obj = request.GET.get('user_id')  
        if user_obj:
            vehicle_objects = vehicle_details.objects.filter(user_id=user_obj, is_deleted=False)
            serializer = vehicle_details_serializer(vehicle_objects, many=True)
            if serializer.data:
                return JsonResponse({"message": f"Vehicle details for id {user_obj} retrieved successfully!!", "data": serializer.data})
            else:
                return JsonResponse({"message": f"No vehicle details found for date {user_obj}"})
        else:
            return JsonResponse({"message": "Invalid User format."}, status=400)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    
from django.utils.dateparse import parse_date
from .serializers import vehicle_details_serializers_by_daterange

from datetime import datetime
 
# Interservice Call for fetching details from Range of Dates given by User
from datetime import datetime
from django.core.paginator import Paginator
 
@api_view(['GET'])
def get_vehicle_details_by_date_range(request):
    try:
        start_date_str = request.GET.get('start_date')
        end_date_str = request.GET.get('end_date')
 
        #parse
        start_date = datetime.strptime(start_date_str, '%d-%m-%Y').date()
        end_date = datetime.strptime(end_date_str, '%d-%m-%Y').date()
 
        vehicle_obj = vehicle_details.objects.filter(created_at__date__range=[start_date,end_date])
 
        serializer = vehicle_details_serializers_by_daterange(vehicle_obj,many=True)
 
        paginator = Paginator(serializer.data, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
 
        return JsonResponse({"message":"Vehicles data retrieved successfully ", 'data':page_obj.object_list})
   
    except Exception as e:
        return JsonResponse({"message":"Something went wrong", "error":str(e)}, status=500)
    

#Retrive the vehicle details by UTC date
# import pytz
# from django.utils import timezone


# @api_view(['GET'])
# def get_vehicle_details_by_UTC_date_range(request):
#     try:
#         start_date_str = request.GET.get('start_date')
#         print(start_date_str)
#         end_date_str = request.GET.get('end_date')
#         print(end_date_str)
 
#         #parse
#         start_date = datetime.strptime(start_date_str, '%d-%m-%Y').date()
#         end_date = datetime.strptime(end_date_str, '%d-%m-%Y').date()
#         print(start_date)
#         print(end_date)

#         #IST time zome
#         def convert_utc_to_ist(utc_datetime):
#             # Define UTC timezone
#             utc_timezone = pytz.timezone('UTC')

#             # Convert UTC datetime to IST timezone
#             ist_timezone = pytz.timezone('Asia/Kolkata')
#             ist_datetime = utc_datetime.astimezone(ist_timezone)

#             return ist_datetime
        
#         Start_date_IST =convert_utc_to_ist(start_date)
#         end_date_IST =convert_utc_to_ist(end_date)

#         #fetch the vehicles details by using IST 
#         vehicle_obj = vehicle_details.objects.filter(created_at__range=[Start_date_IST,end_date_IST])
 
#         serializer = vehicle_details_serializers_by_daterange(vehicle_obj,many=True)

#         response_data = serializer.data
#         for item in response_data:
#             created_at_ist = datetime.strptime(item['created_at'],'%d-%m-%Y %H:%M')
#             created_at_utc = created_at_ist.astimezone(pytz.utc)
#             item['created_at'] = created_at_utc.strftime('%d-%m-%Y %H:%M')
 
#         return JsonResponse({"message":"Vehicles data retrieved successfully ", 'data':response_data})
   
#     except Exception as e:
#         return JsonResponse({"message":"Something went wrong", "error":str(e)}, status=500)
    
from datetime import datetime
import pytz
from .serializers import vehicle_details_serializers_by_daterange_UTC

@api_view(['GET'])
def get_vehicle_detals_by_UTC_date_format(request):

    start_date=request.GET.get('start_date')
    end_date=request.GET.get('end_date')

    #define the zone 
    utc_timezone = pytz.utc
    ist_timezone = pytz.timezone('Asia/Kolkata')

    #UTC datetime zone
    start_date_utc_datetime = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S').replace(tzinfo=utc_timezone)
    end_date_utc_datetime = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S').replace(tzinfo=utc_timezone)

    #IST timezone 
    start_ist_datetime = start_date_utc_datetime.astimezone(ist_timezone)
    end_ist_datetime = end_date_utc_datetime.astimezone(ist_timezone)

    #parse
    ist_start_date_str = start_ist_datetime.strftime('%Y-%m-%d %H:%M:%S.%f%z')
    ist_end_date_str = end_ist_datetime.strftime('%Y-%m-%d %H:%M:%S.%f%z')

    #fetch details f vehicles
    vehicle_obj = vehicle_details.objects.filter(created_at__range=[ist_start_date_str,ist_end_date_str])

    serializer=vehicle_details_serializers_by_daterange_UTC(vehicle_obj,many=True)

    response_data = serializer.data
    for item in response_data:
            created_at_ist = datetime.strptime(item['created_at'],'%d-%m-%Y %H:%M')
            created_at_utc = created_at_ist.astimezone(pytz.utc)
            item['created_at'] = created_at_utc.strftime('%d-%m-%Y %H:%M')

    return JsonResponse({"message":"vehicle detals successfully added in UTC format","Data":response_data})


        
from datetime import datetime, timedelta
@api_view(['GET'])
@csrf_exempt
def get_vehicle_details_utc(request):
    try:
        start_date_str = request.GET.get('start_date')
        end_date_str = request.GET.get('end_date')
 
        #parse
        start_date = datetime.strptime(start_date_str, '%d-%m-%Y').date()
        end_date = datetime.strptime(end_date_str, '%d-%m-%Y').date()

        duration_to_add = timedelta(hours=5, minutes=30)

        start_date_IST = start_date + duration_to_add
        end_date_IST =end_date + duration_to_add

 
        vehicle_obj = vehicle_details.objects.filter(created_at__date__range=[start_date_IST,end_date_IST])
 
        serializer = vehicle_details_serializers_by_daterange(vehicle_obj,many=True)
 
        
 
        return JsonResponse({"message":"Vehicles data retrieved successfully ", 'data':serializer.data})
   
    except Exception as e:
        return JsonResponse({"message":"Something went wrong", "error":str(e)}, status=500)


            
            

            
    




