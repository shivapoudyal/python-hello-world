from django.conf.urls import url
from django.contrib import admin
from home import views
from restapi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stockSellerProductsModel', views.stockSellerProductsView)

urlpatterns = [
    url('', views.stockSellerProductsView)
]
