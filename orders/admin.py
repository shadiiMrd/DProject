from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    inlines = [OrderItemInline]


admin.site.register(Order , OrderAdmin)
admin.site.register(OrderItem)
