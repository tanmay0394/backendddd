from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import generics
from .models import Catalogue, ProductCategory, CatalogueProductMapping
from .serializers import CatalogueSerializer, ProductCategorySerializer, CatalogueProductMappingSerializer

from . import serializers
from .renderers import UserRenderer


# Create your views here.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegisterView(generics.CreateAPIView):
    serializer_class = serializers.UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserRegisterSerializer(data=request.data)
        if not serializer.is_valid():
            messages: dict = {}
            for key, value in dict(serializer.errors).items():
                messages[key] = value[0]
            return Response(data={'messages': messages, 'status': {'msg': 'failed', 'code': 220}},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token': token, 'message': 'Registration Successful.',
                         'status': {'code': 200, 'msg': 'success'}}, status=status.HTTP_200_OK)


class UserLoginView(generics.CreateAPIView):
    serializer_class = serializers.UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            messages: dict = {}
            for key, value in dict(serializer.errors).items():
                messages[key] = value[0]
            return Response(data={'messages': messages, 'status': {'msg': 'failed', 'code': 220}})

        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response(
                {'token': token, 'message': 'Login Successful.', 'status': {'msg': 'success', 'code': 200}},
                status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Username or Password is not Valid',
                             'status': {'msg': 'success', 'code': 230}}, status=status.HTTP_404_NOT_FOUND)


class HomeView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        return Response(data={'message': 'You are authenticated', 'username': request.user.username},
                        status=status.HTTP_200_OK)
    

#catalogue
    

class CatalogueCreateView(generics.CreateAPIView):
    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer

class CatalogueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer
    lookup_url_kwarg = 'id'

class CatalogueUploadView(generics.CreateAPIView):
    
    pass# HERE WE WILL PREPOPULATE DATA AND ML INTEGARATION WE WILL DO HERE
