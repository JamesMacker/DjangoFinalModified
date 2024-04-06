# serializers.py
from rest_framework import serializers
from .models import humidity
from .models import temperature
from .models import airQuality
from .models import time

class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = humidity
        fields = '__all__'

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = temperature
        fields = '__all__'

class AirQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = airQuality
        fields = '__all__'

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = time
        fields = '__all__'

