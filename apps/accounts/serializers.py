from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, exceptions

from apps.accounts.models import User


class SigninUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'access_level', 'photo', 'is_active', 'created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_active', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)

        errors = dict()
        try:
            validate_password(password)
            user.set_password(password)
            user.save()
            return user
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

    def update(self, instance, validated_data):
        validated_data.pop('password') if validated_data.get(
            'password', False) else None
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
