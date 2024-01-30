from django.db import models


class AboutPage(models.Model):
    title = models.CharField(max_length=150)
    introdcution = models.TextField()
    location = models.TextField()
    services = models.TextField()

    def __str__(self):
        return self.title[:25]

    def __str__(self):
        return self.introdcution[:25]

    def __str__(self):
        return self.location[:25]

    def __str__(self):
        return self.services[:25]
