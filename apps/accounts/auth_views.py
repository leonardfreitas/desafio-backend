from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenViewBase

from .auth_serializers import (
    CustomTokenObtainPairSerializer,
)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
