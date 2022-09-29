from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAdmin

from .serializers import UserSerializer
from apps.accounts.models import User


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
