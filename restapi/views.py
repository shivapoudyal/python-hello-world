# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from restapi.serializer import stockSellerProductSerializer
from restapi.models import stockSellerProductsModel
from rest_framework import viewsets

# Create your views here.

class stockSellerProductsView(viewsets.ModelViewSet):
    queryset = stockSellerProductsModel.objects.raw('select ts.id, tsp.product_name, tsl.seller_name from tib2bw_stock ts LEFT JOIN tib2bw_subscribed_product tsp ON ts.subscribed_product_id = tsp.id LEFT JOIN tib2bw_sellers tsl ON ts.seller_id = tsl.seller_id WHERE ts.id = 39476')
    serialzer_class = stockSellerProductSerializer