from api.serializers import DocumentSerializer
from api.models import Documents
from api.serializers import DocumentSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from api.models import Documents

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
def documentApi(request, id=0):
    if request.method=='GET':
        documents = Documents.objects.all()
        documents_serializer = DocumentSerializer(documents, many=True)
        return JsonResponse(documents_serializer.data, safe=False)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def documentDetails(request, id):
    if request.method == 'GET':
        document = Documents.objects.get(DocumentID=id)
        serializer = DocumentSerializer(document)
        return JsonResponse(serializer.data)

    elif request.method=='POST':
        document_data = JSONParser().parse(request)
        documents_serializer = DocumentSerializer(data=document_data)
        if documents_serializer.is_valid():
            documents_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        document = Documents.objects.get(DocumentID=id)
        # document_data = JSONParser().parse(request)
        documents_serializer = DocumentSerializer(document, data=request.data)
        if documents_serializer.is_valid():
            documents_serializer.save()
            return Response(documents_serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        document = Documents.objects.get(DocumentID=id)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def usersApi(request, id=0):
    if request.method=='POST':
        users_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(("Failed to Add" + users_data), safe=False)
    elif request.method=='GET':
        user_data = User.objects.all()
        user_serializer = UserSerializer(user_data, many=True)
        return JsonResponse(user_serializer.data, safe=False)
