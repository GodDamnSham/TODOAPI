from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets
#from rest_framework import permissions
from todo.serializers import UserSerializer
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer
from rest_framework import generics
from django.contrib.auth import logout
from django.contrib import auth,messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken , OutstandingToken , BlacklistedToken
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    #permission_classes =[IsAuthenticated]


# @csrf_exempt
# @require_http_methods(["POST"])
# def Login(request):
#     print(request)
#
#     serializer_class = MyTokenObtainPairSerializer
#     return JsonResponse({"data": "test"})

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

''' class Logout(APIView):
    def logout_view( self , request):
       logout(request)
       return Response(status=status.HTTP_200_OK) '''



class Logout(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            # request.user.auth_token.delete()
            auth.logout(request)

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

            #return username + token currently loged in 


class LogoutAllView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)
 