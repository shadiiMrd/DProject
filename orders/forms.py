from django import forms
from orders.models import Order, OrderItem


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



class AddOrderForm(BaseModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'table']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تماس'}),
            'table': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'میز'})
        }


class SearchForm(forms.Form):
    search = forms.CharField(required=False  ,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'جستوجو'}))

