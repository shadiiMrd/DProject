from re import search

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from kitchen.forms import SearchForm
from orders.models import Order


@login_required(login_url='accounts:login')
def kitchen_list(request):
    if request.user.is_admin:
        orders = Order.objects.filter(status=Order.ORDER_STATUS[1][0])
    else:
        orders = Order.objects.filter(status=Order.ORDER_STATUS[1][0] , user=request.user)

    search_form = SearchForm()
    search = request.GET.get('search')
    if search:
        orders = orders.filter(Q(name__icontains=search))

    return render(request, "kitchen/list.html",
                  {'orders': orders, 'search_form': search_form})


@login_required(login_url='accounts:login')
def kitchen_change_status(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order, id=order_id)
        order.status = Order.ORDER_STATUS[2][0]
        order.save()
    return redirect('kitchen:kitchen_list')
