from django.contrib.auth.models import User
from django.db import models

class UserSaaS(User):

    def __str__(self):
        return self.username