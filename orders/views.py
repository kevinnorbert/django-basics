from product.views import view_product
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
    product_codes_exists = True
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
        product_codes = []
        for line in lines:
            product_code = line['product_code']
            product_codes.append(product_code)
        products = Product.objects.filter(code__in=product_codes).values_list('code', flat=True)
        #Product.objects.filter(unit_price__contains=20)
        print(products)

        for line in lines:
            request_product_code = line['product_code']            
            if not request_product_code in products:
                product_codes_exists = False
                response = {
                    "message": f"Product {request_product_code} does not exist",
                    "status": False
                }
                break
        if product_codes_exists:
            try:
                order_object = Order()
                order_object.customer_name = customer_name
                order_object.order_no = request_json['order_no']
                order_object.grand_total = request_json['grand_total']
                order_object.save()
                for line in lines:
                    order_line_object = OrderLine()
                    order_line_object.order = order_object
                    order_line_object.product_name = line['product_name']
                    order_line_object.product_code = line['product_code']
                    order_line_object.unit_price = line['unit_price']
                    order_line_object.qty = line['qty']
                    order_line_object.tax_rate = line['tax_rate']
                    order_line_object.save()
                
                
                response = {
                    "message": "Order saved successfully",
                    "status": True,
                    "order-no": order_object.order_no
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

def view_order(request):
    return render(request, 'view_order.html')
       

