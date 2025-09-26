from django.shortcuts import render, HttpResponse
from .models import Car


def index(request):
    return HttpResponse("Hello, world! This is the car rental service.")

def cars(request):
    # This function would typically retrieve car data from the database
    # and render it in a template. For now, we'll just return a simple response.
    cars = Car.objects.all()  # Fetch all car objects from the database
    context = {
        'cars': cars  # Pass the car objects to the template context
    }
    return render(request, 'cars/cars.html', context)
def car_detail(request, car_id):
    # This function would typically retrieve a specific car by its ID
    # and render its details in a template. For now, we'll just return a simple response.
    try:
        car = Car.objects.get(id=car_id)  # Fetch the car object by ID
        context = {
            'car': car  # Pass the car object to the template context
        }
        return render(request, 'cars/car_detail.html', context)
    except Car.DoesNotExist:
        return HttpResponse("Car not found", status=404)