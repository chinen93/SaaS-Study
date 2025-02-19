
from rest_framework import viewsets

from users.models import UserSaaS
from users.serializer import UserSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserSaaS.objects.all()
    serializer_class = UserSerializer