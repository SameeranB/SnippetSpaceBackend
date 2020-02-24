from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

import Snippets
from SnippetSpaceBackend.permissions import HasPermissions


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippets.objects.all()
    lookup_field = 'username'

    permission_classes = [IsAuthenticated, HasPermissions]