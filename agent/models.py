# from organization.models import organization
from calendar import TUESDAY
from django.db.models.deletion import CASCADE
from customer.models import user_profile
from django.db import models
from django.contrib.auth.models import User
# # Create your models here.

class agent(models.Model):
    # agent = models.OneToOneField(User,on_delete=CASCADE, primary_key=True)
    agent_id = models.AutoField(auto_created=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #here onetoonefield changed in foreighn key by aftab..
    service_provider = models.CharField(max_length=30, null=True)
    supervisor_username = models.CharField(max_length=100,default="")
    balance_amount = models.FloatField(default=0)
    bank_acc_no = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=30)
    bank_acc_name = models.CharField(max_length=50)
    bank_ifsc = models.CharField(max_length=20)
    agent_is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return str(self.user)

# class org_agent(models.Model):
#     org_agent_id = models.ForeignKey(User,on_delete=models.CASCADE)
#     org_id = models.ForeignKey(organization, on_delete=models.CASCADE)


