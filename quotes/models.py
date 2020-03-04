from django.db import models

# Create your models here.


class Stock(models.Model):
    ticker = models.TextField()
    tickerlong = models.TextField()

    def __str__(self):
        return self.ticker