from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_name = models.CharField(max_length=34)
    # user_photo = models.ImageField()
    user_photo = models.ImageField(upload_to='images/profileimage/', default="images/profileimage/default_profile_img.jpg", null=True)
    user_type = models.CharField(max_length=20, default="customer")
    is_agent = models.BooleanField(default=False)
    user_phone = models.IntegerField(null=True)
    user_email = models.EmailField(null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    wallet_amt = models.FloatField(default=0)

