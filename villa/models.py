from django.db import models
from client.models import Client


# Create your models here.


class VillaBooking(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    booking_date = models.DateField()
    leave_date = models.DateField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
