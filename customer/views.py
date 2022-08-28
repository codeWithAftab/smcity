from customer.serializers import user_profile_serializer
from customer.models import user_profile
from django.core.checks.messages import Error
from django.http.response import HttpResponse
from django.shortcuts import render
import django.contrib.auth
# User = django.contrib.auth.get_user_model()
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# user = User.objects.create_user('username', password='userpassword')
# user.is_superuser = False
# user.is_staff = False
# user.save()
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from charzer import settings

def home(request):
    return HttpResponse("<center><h1>Welcome To smart City....</h1><h3> This is a rest api so hit endpoints and get corresponding data...</h3></center> ")

class user_register(APIView):

    def put(self, request):
        try:
            username = request.data.get('username')
            if User.objects.filter(username=username).exists():

                msg = {
                    "msg": "username-not-available",
                    "resp":"stop"
                }
                return Response(msg)
                pass
            else:
                msg = {
                    "msg": "username-available",
                    "resp":"proceed"
                }

                return Response(msg)

        except Exception as e:
            msg ={
                "resp":"fail",
                "msg": f"{e}"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)


    def post(self,request):
        try:
            gusername = request.data.get('username')
            if User.objects.filter(username=gusername).exists():
                msg = {
                    "msg": "not-available",
                    "resp":"username-not-available"
                }

                return Response(msg,status=status.HTTP_400_BAD_REQUEST)

            else:
                username = request.data.get('username')
                password = request.data.get('password')
                if username != None and password!=None:
                    try:
                        user = User.objects.create_user(username, password=password)
                        user.is_superuser = False
                        user.is_staff = False
                        user.save()
                        u = user_profile(user=user, user_name=user.username)
                        u.save()

                        # print(token.key)
                    except Exception as e:
                        return Response({"msg":f"hey {e}","resp":"fail"},status=status.HTTP_400_BAD_REQUEST)

                    token = Token.objects.create(user=user)
                    return Response({"msg":"created user successfully","resp":"successful","token": str(token)})
                else:
                    return Response({"msg":"username and password cannot be None","resp":"failed"})


        except Exception as e:
            msg ={
                "resp":"fail",
                "msg": f"{e}"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)


class user_profile_api(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes  = [IsAuthenticated]

    def get(self, request):
        try :
            u = user_profile.objects.get(user=request.user)
            print("here",u)
            serializer = user_profile_serializer(u)
            dat = serializer.data
            dat["user_photo"] = settings.website_name + dat["user_photo"]
            return Response(dat)
        except Exception as e:
            return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self, request):
        try:
            user = user_profile.objects.get(user=request.user)
            serializer = user_profile_serializer(user,data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            msg ={
                "resp":"fail",
                "msg": f"{e}"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)


# from django.http import JsonResponse
# class user_login(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes  = [IsAuthenticated]

#     def get(self, request):
#         # username = request.data.get('username')
#         # password = request.data.get('password')
#         msg = {
#             "hello":"world"
#         }
#         # return HttpResponse('{"hello":"world"',content_ty)
#         return Response(msg)

# from rest_framework.decorators import api_view

# @api_view()
# def temp(request):
#     u = user_profile.objects.all()
#     st = user_profile_serializer(u)
#     return Response(st.data)