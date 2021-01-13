# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from serializers import teamSerializers

from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.models import Ourteams
from home.models import teams
from home.models import my_custom_sql
from home.models import teamcrud

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Homepage!")

def about(request):
    
    teamsmembers = teams.objects.all()

    data = {'teams':teamsmembers}
    return render(request, 'about.html',data)
    # return HttpResponse(teamsmembers)  


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        storedate = datetime.today()

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Details has been saved!')

    return render(request, 'contact.html')

def test(request):
    return render(request, 'test.html')

def testoperations(request):
    num1 = int(request.POST["num1"])
    num2 = int(request.POST["num2"])
    data = {
        'result': num1 + num2
    }
    return render(request, 'result.html', data)

def tables(request):
    return render(request, 'tables.html')

@api_view(['GET', 'POST'])
def api(request):
    if request.method == "GET":
        obj = teamcrud.objects.all().order_by('-id')
        serializer = teamSerializers(obj, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = teamSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)        
        
@api_view(['GET'])
def team_details(request, teamId):
    try:
        obj = teams.objects.get(id =teamId)
    except teams.DoesNotExist:
        return Response(status = status.HTTPS_404_NOT_FOUND)
    serializer = teamSerializers(obj)
    return Response(serializer.data)


