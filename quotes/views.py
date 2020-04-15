#Copyright (c) 2020 Jalen Ross, all rights reserved

from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm, SignUpForm
from django.contrib import messages

# for authentication
from django.contrib.auth import login, authenticate

# for email sending
from stocks.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

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
        form = StockForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            messages.success(request, ("Ticket has been listed!"))
            return redirect('add_stock')

    else:    
        form = "noform"
    ticker = Stock.objects.all()
    return render(request, 'add_stock.html', {'ticker': ticker, 'form': form})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    seller_name = item.user_whole_name
    event = item.tickerlong
    buyer_email = request.user.email
    buyer_name = request.user.get_full_name()

    #send email
    subject = "Your ticket transaction, via FireSaleHBS"
    message = "Dear users, we've found a ticket transaction for you! " \
        + "</br></br>" + buyer_name + " would like to buy a ticket for " + event + " from " + seller_name + ".  Congrats on the match!" \
        + "</br></br>You can use this email (you're both copied) to coordinate transfer and payment." \
        + "</br></br>Thank you for using <a href='www.firesalehbs.com'>FireSaleHBS</a>!"
    recepient = [buyer_email, "jalenjjbr@gmail.com"]
    send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently = False)

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