from apps.users.models import UserSaaS
from apps.users.serializer import UserSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserSaaS.objects.all()
    serializer_class = UserSerializer
