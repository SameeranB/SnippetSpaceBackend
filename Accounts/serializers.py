from rest_framework import serializers

from Accounts.models import User
from SnippetSpaceBackend import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'confirm_password']

    def validate_password(self, value):
        data = self.get_initial()

        if data.get('confirm_password') != value:
            raise serializers.ValidationError("The two passwords do not match.")
        return value


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('favorite_language',)
