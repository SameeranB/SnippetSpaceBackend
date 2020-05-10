# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from SnippetSpaceBackend.permissions import HasPermissions
from Snippets.models import Snippet
from Snippets.serializers import SnippetSerializer


class SnippetViewSet(viewsets.GenericViewSet,
                     viewsets.mixins.RetrieveModelMixin,
                     viewsets.mixins.CreateModelMixin,
                     viewsets.mixins.ListModelMixin):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    lookup_field = 'snippet_id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['framework', 'author']

    permission_classes = [AllowAny, HasPermissions]

    def list(self, request, *args, **kwargs):
        return super(SnippetViewSet, self).list(self, request, *args, **kwargs)



    def create(self, request, *args, **kwargs):
        serializer_data = self.get_serializer(data=request.data)
        if serializer_data.is_valid():
            snippet = serializer_data.save(author=request.user)
            request.user.contributions += 1
            request.user.save()
            return Response({'message': "Snippet saved successfully", 'snippet_id': snippet.snippet_id}, status=201)
        else:
            return Response({'error': serializer_data.errors})
