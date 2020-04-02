from rest_framework import serializers

from Accounts.models import User
from Snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField()
    class Meta:
        model = Snippet
        fields = '__all__'
        read_only_fields = ['author']


