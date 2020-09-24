from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name',
                  'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

# def update(self, instance, validated_data):
#     instance.username = validated_data.get('username', instance.username)
#     instance.email = validated_data.get('email', instance.email)
#     instance.first_name = validated_data.get('first_name',
#  instance.first_name)
#     instance.last_name = validated_data.get('last_name', instance.last_name)
#     instance.save()
#     return instance
