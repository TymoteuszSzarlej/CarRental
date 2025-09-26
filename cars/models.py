from django.db import models

# Create your models here.

class Car(models.Model):
    EQUIPMENT_CHOICES = [
        ('GPS', 'GPS'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Heated Seats', 'Heated Seats'),
        ('Bluetooth', 'Bluetooth'),
        ('Sunroof', 'Sunroof'),
    ]

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    fuel_usage = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage_limit = models.PositiveIntegerField()
    value = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    insurance_expiry_date = models.DateField()
    equipment = models.CharField(max_length=50, choices=EQUIPMENT_CHOICES)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.brand + ' ' + self.model