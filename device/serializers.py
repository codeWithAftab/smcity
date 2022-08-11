from django.db import models
from django.db.models import fields
from rest_framework import serializers 
from device.models import device, dustbin, washroom, waterpoint

class deviceserializer(serializers.ModelSerializer):
    class Meta:
        model = device
        # fields = "__all__"
        fields = ["device_id","device_lat", "device_long", "is_active","device_mac", "device_type","privlaged_user"]
        


class dustbinserializer(serializers.ModelSerializer):
    class Meta:
        model = dustbin
        # fields = "__all__"
        fields = ["dustbin_level"]

class waterpointserializer(serializers.ModelSerializer):
    class Meta:
        model = waterpoint
        # fields = "__all__"
        fields = ["water_level"]
class washroomserializer(serializers.ModelSerializer):
    class Meta:
        model = washroom
        fields = "__all__"


class deviceserializer(serializers.ModelSerializer):
    class Meta:
        model = device
        # fields = "__all__"
        fields = ["device_id","device_lat", "device_long", "is_active","device_mac", "device_type","privlaged_user"]
        

# Update API's

class updatedeviceserializer(serializers.ModelSerializer):
    class Meta:
        model = device
        # fields = "__all__"
        fields = ["device_lat", "device_long", "is_active","device_type","privlaged_user"]
 

class updatedustbinserializer(serializers.ModelSerializer):
    class Meta:
        model = dustbin
        # fields = "__all__"
        fields = ["dustbin_level"]

class updatewaterpointserializer(serializers.ModelSerializer):
    class Meta:
        model = waterpoint
        # fields = "__all__"
        fields = ["water_level"]
class updatewashroomserializer(serializers.ModelSerializer):
    class Meta:
        model = washroom
        fields = "__all__"