from django.contrib.auth.forms import ReadOnlyPasswordHashField
from captcha.fields import CaptchaField
from .models import *
from django import forms


class BaseForm(forms.Form):
    default_error_messages = {
        'required': 'این فیلد اجباری است',
        'invalid': 'مقدار وارد شده معتبر نیست',
        'invalid_choice': 'گزینه انتخاب شده معتبر نیست',
        'unique': 'کاربری با این ایمیل از قبل وجود دارد',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = self.default_error_messages.copy()  # Fixed typo


class BaseModelForm(forms.ModelForm):
    default_error_messages = {
        'required': 'این فیلد اجباری است',
        'invalid': 'مقدار وارد شده معتبر نیست',
        'invalid_choice': 'گزینه انتخاب شده معتبر نیست',
        'unique': 'کاربری با این ایمیل از قبل وجود دارد',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = self.default_error_messages.copy()


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'position', 'email', 'phone_number')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password1'] and data['password2'] and data['password1'] != data['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return data['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password1 = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'position', 'email', 'phone_number')

    def clean_password2(self):
        return self.initial['password']


class LoginForm(BaseForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': 'شماره موبایل'}),
                                   label='موبایل')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'پسورد'}), label='پسورد')
    remember_me = forms.BooleanField(required=False, label='مرا به خاطر بسپار')


class EditProfile(BaseModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number')

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'phone_number': 'شماره تماس',
        }
