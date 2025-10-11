from django import forms
from wait.models import Wait


class AddWaitForm(forms.ModelForm):
    class Meta:
        model = Wait
        fields = ['name', 'phone_number' , 'facility']

        labels={
            'name':'نام',
            'phone_number':'شماره تماس',
            'facility':'امکانات'
        }