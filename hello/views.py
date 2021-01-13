from django.shortcuts import render
from hello.serializer import stockSellerProductSerializer, crudtestSerializer
from hello.models import stockSellerProductsModel, crudtestModel
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class stockSellerProductsView(viewsets.ModelViewSet):
    queryset = stockSellerProductsModel.objects.raw('select ts.id, tsp.product_name, tsl.seller_name from tib2bw_stock ts LEFT JOIN tib2bw_subscribed_product tsp ON ts.subscribed_product_id = tsp.id LEFT JOIN tib2bw_sellers tsl ON ts.seller_id = tsl.seller_id WHERE ts.id = 39476')
    serializer_class = stockSellerProductSerializer

class crudtestView(viewsets.ModelViewSet):
    queryset = crudtestModel.objects.all()
    serializer_class = crudtestSerializer

