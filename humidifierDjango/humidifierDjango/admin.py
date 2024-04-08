from django.contrib import admin
from humidifierDjango.models import humidity, temperature, tvoc, time
# Register your models here.
admin.site.register(humidity)
admin.site.register(temperature)
admin.site.register(tvoc)
admin.site.register(time)