from lib2to3.pgen2 import token
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

#from rest_framework.authtoken.models import Token

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user','id', 'username','first_name','last_name', 'email', 'password')
        extra_kawrgs = {'password': {'write_only': True , 'required':True}}

    ''' def create(self, validated_data):
        user = User.objects.create_user(
        username=validated_data['username'],
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        Token.objects.create(user=User)
        return user   '''

def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user  

''' class taskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'aufgabe','aufgabeBeschreibung','date')
       
def create(self, validated_data):
        task = Task.objects.create_user(**validated_data)
        return task  '''

        


class   MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','first_name','last_name', 'email', 'password')
        extra_kawrgs = {'password': {'write_only': True , 'required':True}}


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user