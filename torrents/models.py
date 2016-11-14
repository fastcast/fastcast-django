from django.db import models
from accounts.models import UserProfile

class Torrent(models.Model):
    pub_date = models.DateField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    torrent_file = models.FileField()
    user = models.ForeignKey(UserProfile)

    def __str__(self):
        return self.name
