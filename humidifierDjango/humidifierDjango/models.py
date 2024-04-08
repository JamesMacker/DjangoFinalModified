from django.db import models

# Create your models here.
class humidity(models.Model):
    humidity_num = models.DecimalField(max_digits=7, decimal_places=4)
    time_created = models.DateTimeField(auto_now_add=True)  # Automatically set the time when object is created
    time_updated = models.DateTimeField(auto_now=True)  # Automatically update the time when object is saved

    def __str__(self):
        return f"Humidity: {self.humidity_num}, Last Updated: {self.time_updated}"
    
class temperature(models.Model):
    temperature_num = models.DecimalField(max_digits= 3, decimal_places = 1)

    def __str__(self):
        return str(self.temperature_num)
    
class tvoc(models.Model):
    tvoc_num = models.DecimalField(max_digits= 4, decimal_places = 1)

    def __str__(self):
        return str(self.tvoc_num)
    
class time(models.Model):
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.time_update)
    
