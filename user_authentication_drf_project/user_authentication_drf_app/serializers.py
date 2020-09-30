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


class UserProfileChangeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False,
                                     allow_blank=True,
                                     initial="current username")

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        print('instance of username', instance.username)
        return instance
