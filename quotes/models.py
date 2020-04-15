from django.db import models

# Create your models here.


class Stock(models.Model):
    ticker = models.TextField()
    tickerlong = models.TextField(default="default")

    date = models.DateField()
    location = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    user = models.User()

    def __str__(self):
        return self.tickerlong