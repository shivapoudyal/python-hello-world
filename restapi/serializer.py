from rest_framework import serializers
from restapi.models import stockSellerProductsModel

class stockSellerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = stockSellerProductsModel
        fields = ['id', 'product_name', 'seller_name']