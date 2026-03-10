from statistics import mode
from django.db import models
from django.contrib.auth.models import User
#models

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address  = models.CharField(max_length=100, default='', null=True, blank=True)
    date_of_birth = models.CharField(max_length=20, default='', null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

