from django.db import models
from datetime import date

# Create your models here.


class Stock(models.Model):
    ticker = models.TextField()
    tickerlong = models.TextField(default="default")

    date = models.DateField(default=date.today)
    location = models.TextField(default="default")
    price = models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
    user_whole_name = models.TextField(default="default")
    seller_email = models.EmailField(default="default@default.com")

    def __str__(self):
        return self.tickerlong