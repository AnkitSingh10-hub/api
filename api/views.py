from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
from .serializers import EmployeeSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def employeeListView(request):
    if request.method == "GET":
        employees = Employee.objects.all()

        serializer = EmployeeSerializer(employees, many=True)
        print(serializer.data)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == "POST":
        # jsonData = JSONParser().parse(request)
        # data = jsonData
        serializer = EmployeeSerializer(data=request.data)
        print(request.data, "Python data type request.data")

        if serializer.is_valid():
            serializer.save()
            print(serializer.data, "Python data type")
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET'])
def UserListView(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['DELETE', 'GET', 'PUT'])
def employeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(id=pk)
        print(employee)
    except Employee.DoesNotExist:
        return Response(status=404)

    if request.method == "DELETE":
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == "GET":
        serializer = EmployeeSerializer(employee, many=False)
        return Response(serializer.data)
    if request.method == "PUT":

        serializer = EmployeeSerializer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data, "Python data type")
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
