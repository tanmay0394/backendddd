from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Catalogue, ProductCategory, CatalogueProductMapping


UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    """user register serializer"""
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """validate referral code is valid and expired or not"""
        return attrs

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'].lower(),
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ["id", "username", "password"]


class UserLoginSerializer(serializers.ModelSerializer):
    """user login serializer"""
    username = serializers.CharField(max_length=255)

    class Meta:
        model = UserModel
        fields = ['username', 'password']

# for catalogue



class CatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogue
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class CatalogueProductMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogueProductMapping
        fields = '__all__'



