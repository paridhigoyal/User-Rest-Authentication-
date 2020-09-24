from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer, UpdateSerializer


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        queryset = User.objects.filter(user=self.request.user)
        return queryset
