from django.db import models


class ServicesModel(models.Model):
    service_page_title = models.CharField(max_length=150)
    name_of_service = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.TextField()

    def __str__(self):
        return f"Services Page Title: {self.service_page_title} - The name of the service:  {self.name_of_service} - Price: {self.price}UGX - Notes about service: {self.comments} "
