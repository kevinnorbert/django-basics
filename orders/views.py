from django.shortcuts import render
from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import json
from orders.models import *
from product.models import Product
from customer.models import Customer

# Create your views here.
@csrf_exempt
def create_order(request):
    customer_exists = False
    body = request.body
    request_json = json.loads(body)
    customer_name = request_json['customer_name']
    try:
        customer_objects = Customer.objects.all()
        for customer_object in customer_objects:
            if customer_object.fullname == customer_name:
                customer_exists = True
                break
        if customer_exists:
            pass
        else:
            response = {
            'message': "Customer doesn't exists",
            'code': 500,
            }
    except IntegrityError:
        response = {
            'message': 'Order no: already exists',
            'code': 500
        }
    return JsonResponse(response, safe=False)
    

