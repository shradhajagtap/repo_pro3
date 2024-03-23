from django.db import models


class OnlineFood(models.Model):
    FOOD_DELIVERY_BREAKFAST = [("TEA", "Tea"), ("COFFEE", "Coffee"), ("POHE", "Pohe"), ("UPMA", "Upma"), ("DOSA", "Dosa")]
    customer_first_name = models.CharField(max_length=20)
    customer_last_name = models.CharField(max_length=20)
    customer_address = models.CharField(max_length=20)
    customer_mobile_no = models.IntegerField()
    food_mode = models.CharField(max_length=20, choices=FOOD_DELIVERY_BREAKFAST)
