from rest_framework import serializers

from Snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = '__all__'