from distutils.sysconfig import EXEC_PREFIX
from functools import partial
from msilib.schema import Class
from operator import truediv
from pstats import Stats
from django.shortcuts import render
# Create your views here.
from agent.models import agent
from rest_framework.serializers import Serializer
# from customer.serializers import user_profile_serializer
from customer.models import user_profile
from django.core.checks.messages import Error
from django.http.response import HttpResponse
from django.shortcuts import render
import django.contrib.auth
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from supervisor.models import sup_agent, supervisor
from supervisor.serializers import add_agent_list, supervisorserializer, supervisorserialzerupdate
import json

class becomeSupervisor(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        try:
            user = user_profile.objects.get(user=request.user)
            if user.is_verified and user.user_type == "customer":
                data = request.data
                s = supervisor(user=request.user, service_provider=data["service_provider"], bank_acc_no=data["bank_acc_no"],
                               bank_name=data["bank_name"], bank_acc_type=data["bank_acc_type"], bank_ifsc=data["bank_ifsc"])
                s.supervisor_is_active = True
                s.save()
                user.is_supervisor = True
                user.user_type = "supervisor"
                user.save()
                msg = {
                    "msg": "you are now a supervisor",
                    "res": "successful"
                }
                # serializer = supervisorserialzer(s)
                serializer = supervisorserializer(s)
                msg.update(serializer.data)
                return Response(msg, status=status.HTTP_200_OK)
            else:
                msg = {
                    "msg": "You are already a supervisor or Your user id is not verified",
                    "res": "fail"
                }
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            msg = {
                "msg": f"{e}",
                "resp": "fail"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)


class supervisorDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = user_profile.objects.get(user=request.user)
            if user.user_type == "supervisor":
                print("############")
                sup = supervisor.objects.get(user=request.user)
            # print(sup)
                serializer = supervisorserializer(sup)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            # print(e)
            return Response({"msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            sup = supervisor.objects.get(user=request.user)
            serializer = supervisorserialzerupdate(
                sup, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                sup = supervisor.objects.get(user=request.user)
                se = supervisorserializer(sup)
                # return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(se.data, status=status.HTTP_200_OK)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


class agentList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            print(request.user)
            user = agent.objects.get(user=request.user)
            print(user)
            data = request.data
            supuser = User.objects.get(username=data["supervisor"])
            sup = supervisor.objects.get(user=supuser)
            # if sup_agent.objects.filter(supervisor=sup):
            #     print("hi")
            #     msg = {
            #         "msg":""
            #     }

            print(sup)
            print(supuser)

            agentLis = sup_agent(agent=user, supervisor=sup)

            agentLis.save()
            print("success")
            msg = {
                "msg": "Your Request sent success fully status pending",
                "status": "pending"
            }
            return Response(msg, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            user = user_profile.objects.get(user=request.user)
            if user.is_supervisor:
                print("############")
                sup = supervisor.objects.get(user=request.user)
                agentlists = list(sup_agent.objects.filter(supervisor=sup))
                myagentLists = []
                for myagent in agentlists:
                    myobj = {}
                    myobj.update(vars(myagent))
                    myobj["supervisorName"] = myagent.supervisor.user.username
                    myobj["agentName"] = myagent.agent.user.username
                    print(myobj["supervisorName"])
                    myobj.pop("_state")
                    myagentLists.append(myobj)
                    print(myobj)
            # serializer = supervisorserializer(sup)
            return Response({"masg":"success","data":json.dumps(myagentLists)}, status=status.HTTP_200_OK)

        except Exception as e:
            # print(e)
            return Response({"msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

        except:
            pass
