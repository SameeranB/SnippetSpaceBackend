from rest_framework import serializers

from SnippetSpaceBackend import settings


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = '__all__'



