from api.models import Documents
from api.serializers import DocumentSerializer, UserSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
def documentApi(request, id=0):
    if request.method=='POST':
        document_data = JSONParser().parse(request)
        documents_serializer = DocumentSerializer(data=document_data)
        if documents_serializer.is_valid():
            documents_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='GET':
        documents = Documents.objects.all()
        documents_serializer = DocumentSerializer(documents, many=True)
        return JsonResponse(documents_serializer.data, safe=False)

@csrf_exempt
def usersApi(request, id=0):
    if request.method=='POST':
        users_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='GET':
        user_data = User.objects.all()
        user_serializer = UserSerializer(user_data, many=True)
        return JsonResponse(user_serializer.data, safe=False)