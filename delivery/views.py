from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from orders.models import Order


@login_required(login_url='accounts:login')
def delivery_list(request):
    if request.user.is_admin:
        orders = Order.objects.filter(status=Order.ORDER_STATUS[2][0])
    else:
        orders = Order.objects.filter(status=Order.ORDER_STATUS[2][0])

    return render(request, 'delivery/list.html',
                  {'orders': orders})


@login_required(login_url='accounts:login')
def change_delivery_status(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order, id=order_id)
        order.status = Order.ORDER_STATUS[3][0]
        order.save()
        return redirect('delivery:delivery_list')
