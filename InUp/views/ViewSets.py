from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from InUp.serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
        permission_classes = (AllowAny,)
        queryset = User.objects.all()
        serializer_class = UserSerializer
