from rest_framework import serializers

from users.models import UserSaaS

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserSaaS
        fields = ['url', 'username', 'email', 'is_staff']