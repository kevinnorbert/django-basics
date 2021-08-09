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
    product_code_exists = True
    body = request.body
    request_json = json.loads(body)
    customer_name = request_json['customer_name']
    
    customer_objects = Customer.objects.all()
    for customer_object in customer_objects:
        if customer_object.fullname == customer_name:
            customer_exists = True
            break
    if customer_exists:
        lines = request_json['lines']
        for line in lines:
            request_product_code = line['product_code']
            product_objects = Product.objects.all()
            product_code_found = False
            for product_object in product_objects:
                if product_object.code == request_product_code:
                    product_code_found = True
                    break
            if not product_code_found:
                product_code_exists = False
                response = {
                    "message": f"Product {request_product_code} does not exist",
                    "status": False
                }
                break
        if product_code_exists:
            try:
                order_object = Order()
                order_object.customer_name = customer_name
                order_object.order_no = request_json['order_no']
                order_object.grand_total = request_json['grand_total']
                order_object.save()
                for line in lines:
                    order_line_object = OrderLine()
                    order_line_object.order_id = order_object.id
                    order_line_object.product_name = line['product_name']
                    order_line_object.product_code = line['product_code']
                    order_line_object.unit_price = line['unit_price']
                    order_line_object.qty = line['qty']
                    order_line_object.tax_rate = line['tax_rate']
                    order_line_object.save()
                
                response = {
                    "message": "Order saved successfully",
                    "status": True
                }
            except IntegrityError:
                response = {
                    "message": "Order already exists",
                    "status": True
                }


                    



    else:
        response = {
        'message': "Customer doesn't exists",
        'code': 500,
        }
    
    return JsonResponse(response, safe=False)
    
