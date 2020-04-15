from django import forms
from .models import Stock
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["tickerlong"]

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='*Required')
    last_name = forms.CharField(max_length=50, required=True, help_text='*Required')
    email = forms.EmailField(max_length=254, help_text='*Required. Please use a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )