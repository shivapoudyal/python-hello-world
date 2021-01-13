from django.conf.urls import url
from django.contrib import admin
from home import views

urlpatterns = [
    # url('', views.index, name='index'),
    url('about', views.about, name='about'),
    url('contact', views.contact, name='contact'),
    url('test', views.test, name='test'),
    url('testoperations', views.testoperations, name='testoperations'),
    url('tables', views.tables, name='tables'),
    url('api/', views.api, name='api'),
    url('api/<int:teamId>/', views.team_details),
]