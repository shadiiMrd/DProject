from django.contrib.admin.templatetags.admin_list import search_form
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from orders.forms import *
from orders.models import Order
from main.models import *


@login_required(login_url='accounts:login')
def list_orders(request):
    orders = Order.objects.filter(user=request.user)

    search_form = SearchForm()
    search = request.GET.get('search')
    if search:
        orders = orders.filter(Q(user__order__name__icontains=search))

    paginator = Paginator(orders, 2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(request, 'orders/list.html',
                  {'orders': orders, 'search_form': search_form,
                   'page_obj': page_obj, 'page_num': page_num})


@login_required(login_url='accounts:login')
def add_order(request):
    menu_order = Menu.objects.all()

    search_form = SearchForm()
    search = request.GET.get('search')
    if search:
        menu_order = menu_order.filter(name__icontains=search)

    paginator = Paginator(menu_order, 2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    if request.method == 'POST':
        add_order_form = AddOrderForm(request.POST)

        if add_order_form.is_valid():
            data_order = add_order_form.cleaned_data

            order = Order.objects.create(
                user_id=request.user.id,
                name=data_order['name'],
                phone_number=data_order['phone_number'],
                table=data_order['table'],
                status=Order.ORDER_STATUS[1][0]
            )

            selected_items = request.POST.getlist('selected_items')
            for menu_id in selected_items:
                count_str = request.POST.get(f'count_{menu_id}', '1')
                try:
                    count = int(count_str)
                except ValueError:
                    count = 1

                OrderItem.objects.create(
                    order=order,
                    menu_id=menu_id,  # use menu_id here
                    count=count
                )

            messages.success(request, 'سفارش با موفقیت ثبت شد', 'success')
            return redirect('orders:list_orders')

    else:
        add_order_form = AddOrderForm()

    return render(request, 'orders/add.html', {
        'add_order_form': add_order_form,
        'menu_order': menu_order,
        'search_form': search_form,
        'page_num': page_num,
        'page_obj': page_obj,
    })
