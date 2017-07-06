from django.db import models

# Create your models here.

class Map(models.Model):
    map_text = 'Hello World from Models!'

    def __str__(self):
        return self.map_text
class Buyer(models.Model):
    buyer_text = ''

class Seller(models.Model):
    seller_text = ''