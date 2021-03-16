from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import *

class UserSerializer(serializers.ModelSerializer):
    # def to_representation(self, value):
    #     return value.username
    class Meta:
        model = User
        fields = ['username']

class AdvisorSerializer(serializers.ModelSerializer):
    # def to_representation(self, value):
    #     return value.name
    class Meta:
        model = Advisor
        fields = ['id','name','photo_url']

class BookingTimeSerializer(serializers.ModelSerializer):
    advisor = AdvisorSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True, many=True)


    class Meta:
        model = BookingTime
        # fields = ['advisor_id','advisor_name','advisor_photo_url','id','time']
        fields = ['id','time','advisor','user']
        # fields='__all__'
    # advisor_id = serializers.CharField(source='advisor.id')
    # advisor_name = serializers.CharField(source='advisor.name')
    # advisor_photo_url = serializers.CharField(source='advisor.photo_url')

# {
#     "username":"venky",
#     "email":"test@fa.com",
#     "password":"testing@123"
# }


# {
# "name":"first",
# "photo_url":"images/advisor1.jpg"
# }


# {
# "time":"2021-04-10 11:47:58-05"
# }

# {
# "username":"tharun",
# "password":"testing@123"
# }