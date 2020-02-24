from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from Accounts.serializers import UserSerializer
from SnippetSpaceBackend import settings
from SnippetSpaceBackend.permissions import HasPermissions


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = settings.AUTH_USER_MODEL.objects.all()
    lookup_field = 'username'

    permission_classes = [IsAuthenticated, HasPermissions]
