from rest_framework import serializers
from accounts.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id', 'username', 'user_type', 'email', 'password'
        )

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result.pop('password', None)
        return result

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
