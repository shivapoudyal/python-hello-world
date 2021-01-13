from django.db import models

class stockSellerProductsModel(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=200)
    seller_name = models.CharField(max_length=200) 


class crudtestModel(models.Model):
    id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=200)
    mrp = models.CharField(max_length=200)
    available_qty = models.CharField(max_length=122)
    status = models.IntegerField(default=1)
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'crud_test'    