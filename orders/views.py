from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from django.contrib.auth.decorators import login_required
from cars.models import Car
from django.shortcuts import get_object_or_404


# Create your views here.
@login_required  # Ensure the user is logged in to access these views
def orders_list(request):
    # Fetch orders for the currently logged-in user
    orders = Order.objects.filter(user=request.user)  # Filter orders by the logged-in user
    return render(request, 'orders/orders_list.html', {'orders': orders})

@login_required  # Ensure the user is logged in to access this view
def order_detail(request, order_id):
    # Fetch a specific order by its ID
    try:
        order = Order.objects.get(id=order_id, user=request.user)  # Ensure the order belongs to the logged-in user
        return render(request, 'orders/order_detail.html', {'order': order})
    except Order.DoesNotExist:
        return render(request, 'orders/order_not_found.html', status=404)  # Render a not found page if the order does not exist

@login_required
def create_order(request):
    if request.GET.get('car_id'):
        car_id = request.GET.get('car_id')
        car = get_object_or_404(Car, id=car_id)
    else:
        car = None

    if request.method == 'POST':
        form = OrderForm(request.POST)
        car = get_object_or_404(Car, id=request.POST.get('car'))
        if form.is_valid():
            order = form.save(commit=False)
            if car:
                order.car = car  # wymuszenie samochodu
            order.user = request.user
            days = (order.end_date - order.start_date).days
            order.total_price = car.price * days
            order.save()
            return redirect('orders_list')
    else:
        form = OrderForm(initial={'car': car})

    return render(request, 'orders/create_order.html', {'form': form, 'car': car})

@login_required  # Ensure the user is logged in to access this view
def cancel_order(request, order_id):
    try:
        order = Order.objects.get(id=order_id, user=request.user)  # Fetch the order for the logged-in user
        order.status = 'cancelled'  # Update the order status to cancelled
        order.save()  # Save the changes to the database
        return render(request, 'orders/order_cancelled.html', {'order': order})  # Render a cancellation confirmation page
    except Order.DoesNotExist:
        return render(request, 'orders/order_not_found.html', status=404)  # Render a not found page if the order does not exist