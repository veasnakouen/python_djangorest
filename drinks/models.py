from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    email = models.EmailField(default='')

    def __str__(self):
        return self.title

    class Meta:
        ordering=['title'] # simple style for order data 