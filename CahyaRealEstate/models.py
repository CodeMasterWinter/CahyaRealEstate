import uuid
from django.db import models


class Address(models.Model):

    PROVINCE_CHOICES = [
        ('EC', 'Eastern Cape'),
        ('FS', 'Free State'),
        ('GP', 'Gauteng'),
        ('KZN', 'KwaZulu-Natal'),
        ('LP', 'Limpopo'),
        ('MP', 'Mpumalanga'),
        ('NC', 'Northern Cape'),
        ('NW', 'North West'),
        ('WC', 'Western Cape'),
    ]

    street = models.CharField(max_length=255)
    suburb = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=3, choices=PROVINCE_CHOICES)


class Listing(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.IntegerField()
    description = models.TextField()
    rooms = models.IntegerField()
    image = models.ImageField(upload_to='properties/')
    bathrooms = models.IntegerField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.rooms} bedroom in {self.address.suburb}, {self.address.city}'
