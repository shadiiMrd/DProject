from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from django.http import JsonResponse
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


def logIn(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(phone_number=data['phone_number'], password=data['password'])
            if user is not None:
                request.session.set_expiry(10000 if data['remember_me'] else 0)
                login(request, user)
                messages.success(request,  "با موفقیت وارد شدید" ,'success')
                return redirect('orders:list_orders')
            else:
                messages.error(request,  'کاربر یافت نشد', 'error')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html',
                  {'form': form})


def logOut(request):
    logout(request)
    return redirect('accounts:login')


def profile(request):
    profile = get_object_or_404(User, id=request.user.id)
    return render(request, 'accounts/profile.html',
                  {'profile': profile})


def edit_profile(request):
    if request.method == "POST":
        form = EditProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = EditProfile(instance=request.user)
    return render(request, 'accounts/edit_profile.html',
                  {'form': form})


class PasswordReset(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'

    def form_valid(self, form):
        # Add logging
        print("Password reset form is valid")
        print(f"Email to send to: {form.cleaned_data['email']}")
        return super().form_valid(form)


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
