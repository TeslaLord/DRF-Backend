from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import dateutil.parser
import jwt,json
from .models import *
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


# @api_view(['POST'])
# def register(request):
#     serializer = User.objects.create(
#        username=request.data['username'],
#        email=request.data['email'],
#        password = make_password(request.data['password']))
#     serializer.save() 
#     return Response()

class LoginView(APIView):
    def post(self,request):
        try:
            username = request.data['username']
            password = request.data['password']
            if not username or not password:
                return Response({"message":"Invalid Data"},status=400)
        except:
            return Response({"message":"Invalid Data"},status=400)
        try:
            user = authenticate(request, username=username, password=password)
            print(user)
            if not user:
                return Response(status=401)

            refresh = RefreshToken.for_user(user)
        except Exception as e:
            print(e)
            return Response({"message":"Wrong username or password. key is username and password"},status=401)
        return Response({"refresh":str(refresh),'user_id':user.id,'access':str(refresh.access_token)},status=200)


class RegisterView(APIView):
    def post(self,request):
        try:
            username = request.data['username']
            password = request.data['password']
            email = request.data['email']
            if not username or not password or not email:
                return Response({"message":"Invalid Data"},status=400)
            user = User(username=username,email=email)
            user.set_password(password)
            user.save()
            refresh = RefreshToken.for_user(user)
        except:
            return Response({"message":"Invalid data. Keys are username, email and password"},status=400)
        return Response({"refresh":str(refresh),'user_id':user.id,'access':str(refresh.access_token)},status=200)

@api_view(['POST'])
def add_advisor(request):
    try:
        serializer = AdvisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(status=200)
        else:
            return Response(status=400)
    except Exception as e:
        return Response(status=400)

    return Response(status=200)

@api_view(['GET'])
def users_list(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data,status=200)
    except:
        return Response(status=400)


@api_view(['GET'])
def advisor_list(request,pk_user=None):
    try:
        advisors = Advisor.objects.filter(user__id=pk_user)
        serializer = AdvisorSerializer(advisors, many=True)
        return Response(serializer.data,status=200)
    except:
        return Response(status=400)

@api_view(['POST'])
def book_advisor(request,pk_user=None,pk_advisor=None):
    try:
        # booking_time = BookingTime.add(user=User.objects.get(id=pk_user),advisor=Advisor.objects.get(id=pk_advisor),time=dateutil.parser.parse(request.data['time']))
        booking_time = BookingTime.objects.create(time=dateutil.parser.parse(request.data['time']))
        booking_time.user.add(User.objects.get(id=pk_user))
        booking_time.advisor.add(Advisor.objects.get(id=pk_advisor))
        booking_time.save()
        advisor = Advisor.objects.get(id=pk_advisor)
        advisor.user.add(User.objects.get(id=pk_user))
        advisor.save()
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=400)

@api_view(['GET'])
def booked_calls(request,pk_user=None):
    try:
        booking = BookingTime.objects.filter(user=User.objects.get(id=pk_user))
        serializer = BookingTimeSerializer(booking,many=True)
        return Response(serializer.data,status=200)
    except:
        return Response(status=400)