from django.contrib.auth.models import User


class UserSaaS(User):

    def __str__(self):
        return self.username
