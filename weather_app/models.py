from django.db import models

# Create your models here.


class Weather(models.Model):
    city_name = models.TextField(max_length=50)

    def __str__(self):
        return self.city_name

