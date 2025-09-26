from django.contrib import admin

# Register your models here.
from .models import Order

admin.site.register(Order)
# This code registers the Order model with the Django admin site, allowing it to be managed through the admin interface.
# The Order model is defined in orders/models.py and includes fields for car, user, start_date, end_date, total_price, and status.
# The admin interface will automatically generate forms for creating and editing Order instances based on this model definition.