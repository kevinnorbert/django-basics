import customer
from django.shortcuts import render
from django.http import JsonResponse, request, response
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Customer

# Create your views here.
@csrf_exempt
def create_customer(request):
    body = request.body
    request_json = json.loads(body)
    print(request_json)
    customer_obj = Customer()
    customer_obj.username = request_json['username']
    customer_obj.fullname = request_json['fullname']
    customer_obj.mobile_number = request_json['mobile_number']
    customer_obj.save()

    response = {
        'message': 'Created successfully',
        'code': 200,
        'id': customer_obj.id
        }

    return JsonResponse(response, safe=False)

@csrf_exempt
def fetch_customers(request):
    customer_objects = Customer.objects.all()
    customers = []
    for customer_obj in customer_objects:
        customer = {
            'id': customer_obj.id,
            'username': customer_obj.username,
            'fullname': customer_obj.fullname,
            'mobile_number': customer_obj.mobile_number
        }
        customers.append(customer)
    response = {
        'message': 'Fetched successfully',
        'code': 200,
        'customers': customers
        }

    return JsonResponse(response, safe=False)

@csrf_exempt
def fetch_single(request):
    body = request.body
    request_json = json.loads(body)
    cust_id = request_json['id']

    #customer_obj = Customer.objects.get(id=cust_id)
    customer_obj = Customer.objects.filter(id=cust_id).first()
    if not customer_obj:
        response = {
            'message': 'Customer with id does not exist',
            'code': 500,  
        }
    else:    
        customer = {
                'id': customer_obj.id,
                'username': customer_obj.username,
                'fullname': customer_obj.fullname
        }
        response = {
            'message': 'Fetched successfully',
            'code': 200,
            'customer': customer
        }

    return JsonResponse(response)

@csrf_exempt
def update_customer(request):
    body = request.body
    request_json = json.loads(body)
    cust_id = request_json['id']
    customer_obj = Customer.objects.filter(id=cust_id).first()
    if not customer_obj:
        response = {
            'message': 'Customer with id does not exist',
            'code': 500,  
        }
    else:
        customer_obj.username = request_json['username']
        customer_obj.fullname = request_json['fullname']
        customer_obj.mobile_number = request_json['mobile_number']
        customer_obj.save()
        
        response = {
            'message': 'Updated successfully',
            'code': 200,
            'id': customer_obj.id,
        }

    return JsonResponse(response, safe=False)
    

@csrf_exempt
def delete_customer(request):
    body = request.body
    request_json = json.loads(body)
    cust_id = request_json['id']
    customer_obj = Customer.objects.filter(id=cust_id).first()
    if not customer_obj:
        response = {
            'message': 'Customer with id does not exist',
            'code': 500,  
        }
    else:
        customer_obj.delete()
        
        response = {
            'message': 'Deleted successfully',
            'code': 200,
        }
    return JsonResponse(response)        

def view_customer(request):
    customer_data = Customer.objects.all()
    return render(request, 'view_customer.html', {'key': customer_data})
