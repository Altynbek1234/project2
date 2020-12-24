from django.db import models

class Phone(models.Model):
    model = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    price = models.IntegerField(auto_created=True)
    def __str__(self):
        return f'{self.model} и цена {self.price}'
