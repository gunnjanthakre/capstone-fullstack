from django.db import models

class Dealer(models.Model):
    full_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    address = models.TextField()
    zip = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    lat = models.FloatField()
    long = models.FloatField()

    def __str__(self):
        return self.full_name

