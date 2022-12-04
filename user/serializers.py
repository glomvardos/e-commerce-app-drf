from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'user_role', 'email', 'password')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            user_role=validated_data.get('user_role', 'CUSTOMER')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, instance):
        ret = super(UserSerializer, self).to_representation(instance)
        del ret['password']
        return ret


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)
        token['user_role'] = user.user_role
        return token


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    # Here in case we need to override.
    pass
