from apps.users.models import UserSaaS
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserSaaS
        fields = ["url", "username", "email", "is_staff"]
