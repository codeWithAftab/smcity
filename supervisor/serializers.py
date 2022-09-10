from pyexpat import model
from statistics import mode
from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import model_meta
from supervisor.models import supervisor, sup_agent

class supervisorserializer(serializers.ModelSerializer):
    class Meta:
        model = supervisor
        fields = ["service_provider","balance_amount","bank_acc_no","bank_name","bank_acc_type","bank_ifsc","supervisor_is_active"]


# class supervisorserialzer(serializers.Serializer):
#     service_provider = serializers.CharField()
#     supervisor_is_active = serializers.BooleanField()

class supervisorserialzerupdate(serializers.ModelSerializer):
    class Meta:
        model = supervisor
        fields = ["service_provider","bank_acc_no","bank_name","bank_acc_type","bank_ifsc"]

class add_agent_list(serializers.ModelSerializer):
    class Meta:
        model = sup_agent
        fields = ["supervisor","agent","status"]