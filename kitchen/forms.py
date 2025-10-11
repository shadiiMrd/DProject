from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'جستوجو'}))