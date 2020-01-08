from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from .models import User ,board,comment
from django.contrib.auth import get_user_model
from rest_framework.views import APIView        
from rest_framework.response import Response   # 응답
from rest_framework import generics ,viewsets         # 
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST 
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,)
from rest_framework.generics import( #APIVIEW
        UpdateAPIView,
        RetrieveAPIView,
        CreateAPIView,
        DestroyAPIView,
        RetrieveUpdateAPIView
)
from rest_framework.permissions import( 
        AllowAny,
        IsAdminUser,
        IsAuthenticatedOrReadOnly,
        IsAuthenticated,

)

from .serializers import(
RegisterSerializer,
LoginSerializer,
OnSerializer,
boardSerializer,
commentSerializer,
)
from knox.models import AuthToken


User = get_user_model()
"""
class profileView(APIView):
    serializer_class = profileSerializer
    permission_classes =[IsAuthenticated]
    def get(self, request):
        data = request.data
        serializer = profileSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    def post(self, request):
        data = request.data
        serializer = profileSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            saved_data = serializer.data
            return Response(saved_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
        
           
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

"""

class boardViewSet(viewsets.ModelViewSet):
    queryset = board.objects.all()
    serializer_class = boardSerializer
    permission_classes = [AllowAny]
    
    
class commentViewSet(viewsets.ModelViewSet):
    queryset = comment.objects.all()
    serializer_class = commentSerializer



class CreateAPIView(generics.CreateAPIView):

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": OnSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )    
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)    
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": OnSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )

class Logout(APIView):
    def logout(self, request):
       # serializer_class = 
        permission_classes = [IsAuthenticated]
        request.user.auth_token.delete()
        logout(request)    

        return Response({"success": _("Successfully logged out.")},
                    status=status.HTTP_200_OK)