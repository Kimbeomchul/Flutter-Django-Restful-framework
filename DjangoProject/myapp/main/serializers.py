from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User ,board , comment
from django.core.validators import ValidationError
from . import models
from django.db.models import Q
from django.contrib.auth import authenticate

User = get_user_model()

"""
class profileSerializer (serializers.ModelSerializer):  # X 
    class Meta:
        model = profile
        fields = '__all__'
   """     
class boardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = board
        fields = ('title','text')
        
class commentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = comment
        fields = ('posting','name','text')



class OnSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        
class RegisterSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(
        username = validated_data['username'],
        email = validated_data['email'],
        password = validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = [
        'username',
        'password',
        'email',
        #'is_superuser',
        ]

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    
    username = serializers.CharField(required=True, allow_blank=False)
    email = serializers.EmailField(label='Email Address',required=False, allow_blank=True)
    token = serializers.CharField(allow_blank=True,read_only=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
            ]
        extra_kwargs = {'password':{"write_only":True}}
        
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("로그인실패")        

    def recheck(self, data):

        email = data.get("email", None)
        username = data.get("username", None)
        password = data.get("password",None)

        if not email and not username :
            raise ValidationError(" valid error ")

        user = User.objects.filter( Q(email=email)| Q(username=username)).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError(" valid error ")

        if user_obj:
            if not user_obj.check_password(password): 
                raise ValidationError(" pwerror ")

        return data
    
