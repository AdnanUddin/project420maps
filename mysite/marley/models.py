from django.db import models

# Create your models here.

class Map(models.Model):
    map_text = 'Hello World from Models!'

    def __str__(self):
        return self.map_text
class Buyer(models.Model):
    name_text = models.CharField(max_length = 100)
    def __str__(self):
        return "".join((str(self.id), ": ", self.name_text))

class Seller(models.Model):
    name = models.CharField(max_length = 100)
    contact = models.EmailField()
    inventory = models.CharField()

class Transaction(models.Model):
    buyer = models.CharField()
    seller = models.CharField() # TODO primary key
    date = models.DateTimeField()
    item = models.CharField()
    price = models.FloatField()