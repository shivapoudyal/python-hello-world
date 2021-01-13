from rest_framework import serializers
from hello.models import stockSellerProductsModel
from hello.models import crudtestModel

class stockSellerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = stockSellerProductsModel
        fields = ['id', 'product_name', 'seller_name'] 

class crudtestSerializer(serializers.ModelSerializer):
    class Meta:
        model = crudtestModel
        fields = "__all__"        