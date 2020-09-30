from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, UserProfileChangeSerializer


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class UserProfileChangeAPIView(generics.UpdateAPIView):
    serializer_class = UserProfileChangeSerializer
    lookup_field = 'username'
