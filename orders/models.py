from django.db import models

# Create your models here.
class Order(models.Model):
    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed')
    ], default='pending')

    def __str__(self):
        return f"Order {self.id} for {self.car} by {self.user}"
    
    def get_rental_duration(self):
        return (self.end_date - self.start_date).days