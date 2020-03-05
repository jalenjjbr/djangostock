from django.db import models

# Create your models here.


class Stock(models.Model):
    ticker = models.TextField()
    tickerlong = models.TextField(default="default")

    def __str__(self):
        return self.tickerlong