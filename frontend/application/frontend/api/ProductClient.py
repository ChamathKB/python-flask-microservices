from itertools import product
from math import prod
from urllib import response
import requests

class ProductClient:
    @staticmethod
    def get_products():
        response = response.get('http://cproduct-service:5002/api/products')
        products = response.json()
        return products

    @staticmethod
    def get_product(slug):
        response = requests.request('GET', url='http://cproduct-service:5002/api/product/'+slug)
        product = response.json()
        return product