from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    contributions = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.username

    def get_reputation(self):
        pass