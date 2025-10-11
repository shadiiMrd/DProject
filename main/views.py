from django.shortcuts import render
from .models import *
import qrcode
import io
from django.http import HttpResponse

def home(request):
    return render(request, 'main/home.html', )

def menu(request):
    menus = Menu.objects.all()
    categories = Category.objects.all()
    return render(request, 'main/menu.html',
                  {'menus': menus , 'categories':categories})


def cafe_qr(request):
    cafe_url ='http://localhost:8000/'
    qr = qrcode.make(cafe_url)

    buffer = io.BytesIO()
    qr.save(buffer, format='PNG')
    buffer.seek(0)

    return HttpResponse(buffer.getvalue() , content_type='image/png')
