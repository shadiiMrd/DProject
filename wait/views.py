from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *


@login_required(login_url='accounts:login')
def wait_list(request):
    if request.user.is_admin:
        wait_lists = Wait.objects.filter(status=Wait.WAIT_STATUS[0][0])
    else:
        wait_lists = Wait.objects.filter(status=Wait.WAIT_STATUS[0][0], user=request.user)
    return render(request, 'wait/list.html',
                  {'wait_lists': wait_lists})


@login_required(login_url='accounts:login')
def wait_add(request):
    if request.method == "POST":
        form = AddWaitForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Wait.objects.create(name=data['name'], phone_number=data['phone_number'],
                                facility=data['facility'], user=request.user)
            messages.success(request, 'با موفقیت اضافه شد.')
            return redirect('wait:wait_list')
    else:
        form = AddWaitForm()
    return render(request, 'wait/add.html',
                  {'form': form})


def wait_change_status(request, wait_id):
    if request.method == "POST":
        wait = get_object_or_404(Wait, id=wait_id)
        status = request.POST.get('status')
        if status:
            wait.status = status
            wait.save()
        return redirect('wait:wait_list')
