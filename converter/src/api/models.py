from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    marketplace_id = models.CharField(max_length=400, null=False)
    queue_name = models.CharField(max_length=400, null=False)
