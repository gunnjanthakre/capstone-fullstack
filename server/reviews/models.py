from django.db import models
from django.utils import timezone

class Review(models.Model):
    name = models.CharField(max_length=255)
    dealership = models.ForeignKey('dealers.Dealer', on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    purchase = models.BooleanField(default=False)
    purchase_date = models.DateField(null=True, blank=True)
    car_make = models.CharField(max_length=100, null=True, blank=True)
    car_model = models.CharField(max_length=100, null=True, blank=True)
    car_year = models.IntegerField(null=True, blank=True)
    sentiment = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.dealership.full_name}"

    @staticmethod
    def analyze_sentiment(review_text):
        positive_words = ['good', 'great', 'excellent', 'fantastic', 'amazing', 'wonderful', 'best']
        negative_words = ['bad', 'terrible', 'awful', 'horrible', 'worst', 'poor']
        text_lower = review_text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        return 'neutral'

