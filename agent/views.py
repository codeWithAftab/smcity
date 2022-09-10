# Create your views here.
from django.shortcuts import render
from customer.models import user_profile
from django.core.checks.messages import Error
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from agent.models import agent
from supervisor.models import sup_agent
from agent.serializers import agentserializer, agentserialzerupdate

class becomeAgent(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes  = [IsAuthenticated]
    def post(self, request):
        try :
            user = user_profile.objects.get(user=request.user)
            print(user)
            if user.is_verified and user.user_type=="customer":
                data = request.data
                print(data)
                a = agent(user=request.user,service_provider=data["service_provider"], bank_acc_no=data["bank_acc_no"], bank_name=data["bank_name"],bank_acc_name=data["bank_acc_name"],bank_ifsc=data["bank_ifsc"])
                a.agent_is_active = True
                a.save()
                user.is_agent = True
                user.user_type = "agent"
                user.save()
                msg = {
                    "msg":"you are now a agent",
                    "res": "successful"
                }
                serializer = agentserializer(a)
                print(serializer.data)
                msg.update(serializer.data)
                return Response(msg, status=status.HTTP_200_OK)
            else:
                msg = {
                    "msg":f"You are already a {user.user_type} or Your user id is not verified",
                    "res":"fail"
                }
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            msg ={
                "msg":f"{e}",
                "resp":"fail"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

class agentdetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes  = [IsAuthenticated]
    def get(sel, request):
        try :
            # user = user_profile.objects.get(user=request.user)
            # if user.user_type == "agent":
            # print("############")
            ag = agent.objects.get(user=request.user)
            print(ag)
            serializer = agentserializer(ag) 
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            # print(e)
            return Response({"msg":f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try :
            ag = agent.objects.get(user=request.user)
            serializer = agentserialzerupdate(ag, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                ag = agent.objects.get(user=request.user)
                se = agentserializer(ag)
                # return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(se.data, status=status.HTTP_200_OK)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"msg":f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

class myrequests(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def post(self, request):
    #     try:
    #         print(request.user)
    #         user = agent.objects.get(user=request.user)
    #         print(user)
    #         data = request.data
    #         supuser = User.objects.get(username=data["supervisor"])
    #         sup = supervisor.objects.get(user=supuser)
    #         # if sup_agent.objects.filter(supervisor=sup):
    #         #     print("hi")
    #         #     msg = {
    #         #         "msg":""
    #         #     }

    #         print(sup)
    #         print(supuser)

    #         agentLis = sup_agent(agent=user, supervisor=sup)

    #         agentLis.save()
    #         print("success")
    #         msg = {
    #             "msg": "Your Request sent success fully status pending",
    #             "status": "pending"
    #         }
    #         return Response(msg, status=status.HTTP_200_OK)

    #     except Exception as e:
    #         return Response({"msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            user = user_profile.objects.get(user=request.user)
            if user.is_agent:
                print("############")
                ag = agent.objects.get(user=request.user)
                agentlists = list(sup_agent.objects.filter(agent=ag))
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
                    return Response({"msg":"success","data":json.dumps(myagentLists)}, status=status.HTTP_200_OK)

        except Exception as e:
            # print(e)
            return Response({"msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

        except:
            pass
