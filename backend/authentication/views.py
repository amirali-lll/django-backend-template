from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class AuthenticationViewSet(GenericViewSet):
    def get_serializer_class(self):
        if self.action == 'login':
            return LoginSerializer
        elif self.action == 'register':
            return RegisterSerializer
        elif self.action == 'info':
            return UserInfoSerilizer
        elif self.action == 'profile':
            return UploadBase64ProfileImageSerializer
        elif self.action == 'change_password':
            return ChangePasswordSerializer
        
    def get_permissions(self):
        if self.action in ['login', 'register']:
            return []
        else :
            return [IsAuthenticated()]
    

    @action(detail=False, methods=['POST'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods= ['GET', 'PUT', 'PATCH'])
    def info(self, request):
        user = request.user
        if request.method == 'GET':
            return Response(UserInfoSerilizer(user).data)
        elif request.method in ['PUT', 'PATCH']:
            serializer = UserInfoSerilizer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        

    @action(detail=False, methods=['POST'])
    def profile(self, request):
        user = request.user
        serializer = UploadBase64ProfileImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=['POST'])
    def change_password(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data, context={'user': user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)