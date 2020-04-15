#Copyright (c) 2020 Jalen Ross, all rights reserved

from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.

def home(request):
    import requests
    import json

    if request.method == 'POST':

        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_fd607a4bb908445f8ebc5a50ecf6c05e")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol above..."})
    


def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)#or None)
        
        if form.is_valid():
            form.save()
            messages.success(request, ("Ticket has been listed!"))
            return redirect('add_stock')

    else:    
    ticker = Stock.objects.all()
    return render(request, 'add_stock.html', {'ticker': ticker})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Ticket has been purchased!"))
    return redirect(add_stock)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('add_stock')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})