from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Accounts.models import User
from Accounts.serializers import UserSerializer, LoginSerializer, SignupSerializer, UserUpdateSerializer
from SnippetSpaceBackend import settings
from SnippetSpaceBackend.permissions import HasPermissions


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Endpoint to retrieve information about all users on the platform"
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Endpoint to retrieve information about a particular user on the platform"
))
@method_decorator(name='me', decorator=swagger_auto_schema(
    operation_description="Endpoint to retrieve information about the current user"
))
@method_decorator(name='login', decorator=swagger_auto_schema(
    operation_description="Endpoint to allow users to login to the service"
))
@method_decorator(name='signup', decorator=swagger_auto_schema(
    operation_description="Endpoint to signup for the service"
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="Endpoint to update user details. For now, we only support the updation of favorite "
                          "language of the user "
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description="Endpoint to update user details. For now, we only support the updation of favorite "
                          "language of the user "
))
class UserViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin):
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = []

    def get_serializer_class(self):
        if self.action == 'login':
            return LoginSerializer
        elif self.action == 'signup':
            return SignupSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return UserUpdateSerializer
        else:
            return UserSerializer

    def get_permissions(self):
        if self.action == 'login' or self.action == 'signup':
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated, HasPermissions]

        return super(UserViewSet, self).get_permissions()

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        """Endpoint to Retrieve the current users details"""
        serializer_data = self.get_serializer(request.user)
        return Response(serializer_data.data, status=200)

    @action(detail=False, methods=['post'])
    def login(self, request, *args, **kwargs):
        """Endpoint to Log the User in Using Session Authentication"""
        serializer_data = self.get_serializer(data=request.data)
        if serializer_data.is_valid():
            username = serializer_data.validated_data.get('username')
            password = serializer_data.validated_data.get('password')

            user = authenticate(username=username, password=password)
            print(user)

            if user is not None:
                token = Token.objects.get_or_create(user=user)
                print(token)
                return Response({'message': "User logged in successfully", 'token': token[0].key}, status=201)
            else:
                return Response({'message': "Invalid credentials"}, status=400)

    @action(detail=False, methods=['post'])
    def signup(self, request, *args, **kwargs):
        serializer_data = self.get_serializer(data=request.data)
        if serializer_data.is_valid():
            user = User.objects.create(
                username=serializer_data.validated_data.get('username'),
                email=serializer_data.validated_data.get('email'),
                first_name=serializer_data.validated_data.get('first_name'),
                last_name=serializer_data.validated_data.get('last_name')
            )
            user.set_password(serializer_data.validated_data.get('password'))
            user.save()

            return Response({'message': 'Signup successful, please log in to continue', 'username': user.username},
                            status=201)
        else:
            return Response({'error': serializer_data.errors}, status=400)

    def logout(self, request, *args, **kwargs):

        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response({'message': "User logged out successfully"}, status=200)
