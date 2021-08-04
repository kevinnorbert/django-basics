from django.shortcuts import render
from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import json
from product.models import Product
# Create your views here.
@csrf_exempt
def create_product(request):
    body = request.body
    request_json = json.loads(body)
    product_object = Product()
    try:
        product_object.name = request_json['name']
        product_object.code = request_json['code']
        product_object.unit_price = request_json['unit_price']
        product_object.save()
        response = {
        'message': 'Created successfully',
        'code': 200,
        'id': product_object.id
        }
    except IntegrityError:
        response = {
        'message': 'Product with same code already exists',
        'code': 500,
        }
    return JsonResponse(response, safe=False)

@csrf_exempt
def fetch_product(request):
    pass

@csrf_exempt
def fetch_single_product(request):
    pass

@csrf_exempt
def update_product(request):
    pass

@csrf_exempt
def delete_product(request):
    pass
