from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from SnippetSpaceBackend.permissions import HasPermissions
from Snippets.models import Snippet
from Snippets.serializers import SnippetSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    lookup_field = 'username'

    permission_classes = [IsAuthenticated, HasPermissions]