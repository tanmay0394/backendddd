from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_details')
    user_id = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    phone_number_verified = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Details"


class OTPVerification(models.Model):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email_id = models.CharField(max_length=250, null=True, blank=True)
    otp = models.CharField(max_length=10)
    is_otp_used = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "OTP Verification"


class SellerDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_seller_details")
    seller_id = models.CharField(max_length=200)
    seller_unique_code = models.TextField()
    store_name = models.CharField(max_length=200)
    address = models.JSONField(null=True, blank=True)
    email_address = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    profile_photo_url = models.CharField(max_length=1000, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Seller Details"








# catalogue
        
class Catalogue(models.Model):
    catalogue_id = models.AutoField(primary_key=True)
    catalogue_name = models.CharField(max_length=255)
    product_category_id = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    createdby = models.IntegerField()
    createdon = models.DateTimeField(auto_now_add=True)
    updatedby = models.IntegerField()
    updatedon = models.DateTimeField(auto_now=True)
    isdeleted = models.BooleanField(default=False)
    seller_id = models.IntegerField()

class ProductCategory(models.Model):
    product_category_id = models.AutoField(primary_key=True)
    product_category_name = models.CharField(max_length=255)

class CatalogueProductMapping(models.Model):
    cpm_id = models.AutoField(primary_key=True)
    catalogue_id = models.ForeignKey('Catalogue', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
