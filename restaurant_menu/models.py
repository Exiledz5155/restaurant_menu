from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# backend, frontend
MEAL_TYPE = (
    ("cold_items", "Cold Items"),
    ("bbq_items", "BBQ Items"),
    ("specials", "Specials")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

PER_POUND = (
    (0, "Regular"),
    (1, "Per Pound")
)

class Item(models.Model):
    # Unique prevents duplicated meals
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    meal_photo = models.ImageField(upload_to='images/', default="empty")
    per_pound = models.IntegerField(choices=PER_POUND, default=0)

    def __str__(self):
        return self.meal

class Info(models.Model):

    title = models.CharField(max_length=1000, unique=True)
    image = models.ImageField(upload_to='images', default="empty")
    description = models.CharField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title