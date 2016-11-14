from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name
