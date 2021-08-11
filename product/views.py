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
        product_object.tax_rate = request_json['tax_rate']
        product_object.save()
        response = {
        'status': True,
        'message': 'Created successfully',
        'code': 200,
        'id': product_object.id
        }
    except IntegrityError:
        response = {
        'status': False,
        'message': 'Product with same code already exists',
        'code': 500,
        }
    return JsonResponse(response, safe=False)

@csrf_exempt
def fetch_product(request):
    product_objects = Product.objects.all()
    products = []
    for product_obj in product_objects:
        product = {
            'id': product_obj.id,
            'name': product_obj.name,
            'code': product_obj.code,
            'unit_price': product_obj.unit_price,
            'tax_rate':product_obj.tax_rate
        }
        products.append(product)
    response = {
        'message': 'Fetched successfully',
        'code': 200,
        'products': products
    }

    return JsonResponse(response, safe=False)

@csrf_exempt
def fetch_single_product(request):
    body = request.body
    request_json = json.loads(body)
    prod_id = request_json['id']

    product_obj = Product.objects.filter(id=prod_id).first()
    if not product_obj:
        response = {
            'message': 'Product with id does not exist',
            'code': 500,  
        }
    else:    
        product = {
            'id': product_obj.id,
            'name': product_obj.name,
            'code': product_obj.code,
            'unit_price': product_obj.unit_price
        }
        response = {
            'message': 'Fetched successfully',
            'code': 200,
            'product': product
        }

    return JsonResponse(response)


@csrf_exempt
def update_product(request):
    body = request.body
    request_json = json.loads(body)
    prod_id = request_json['id']
    product_obj = Product.objects.filter(id=prod_id).first()
    if not product_obj:
        response = {
            'message': 'Product with id does not exist',
            'code': 500,  
        }
    else:
        try:
            product_obj.name = request_json['name']
            product_obj.code = request_json['code']
            product_obj.unit_price = request_json['unit_price']
            product_obj.save()
            response = {
                'message': 'Updated successfully',
                'code': 200,
                'id': product_obj.id,
            }
        except IntegrityError:
            response = {
            'message': 'Product with same code already exists',
            'code': 500,
            }

    return JsonResponse(response, safe=False)

@csrf_exempt
def delete_product(request):
    body = request.body
    request_json = json.loads(body)
    prod_id = request_json['id']
    product_obj = Product.objects.filter(id=prod_id).first()
    if not product_obj:
        response = {
            'message': 'Product with id does not exist',
            'code': 500,  
        }
    else:
        product_obj.delete()
        response = {
            'message': 'Deleted successfully',
            'code': 200,
        }
    return JsonResponse(response)

def view_product(request):
    #customer_data = Customer.objects.all()
    return render(request, 'view_product.html')
