from django.db import models
from django.contrib.auth.models import User

# # Create your models here.

class organization(models.Model):
    organization_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=123)  #here onetoonefield changed in foreighn key by aftab..
    balance_amount = models.FloatField(default=0)
    bank_acc_no = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    bank_acc_type = models.CharField(max_length=50,default="saving")
    bank_ifsc = models.CharField(max_length=30)
    org_is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class organization_agent_list(models.Model):
    organisation = models.ForeignKey(organization, on_delete=(models.CASCADE))
    org_agent_phone = models.IntegerField()


