from django.db import models


class HomePost(models.Model):
    artist = models.CharField(max_length=50, blank=True)
    art = models.FileField(upload_to="uploads")
    info = models.CharField(max_length=150, blank=True)



