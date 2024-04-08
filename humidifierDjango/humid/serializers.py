# serializers.py
from rest_framework import serializers
from .models import humidity
from .models import temperature
from .models import tvoc
from .models import time

class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = humidity
        fields = '__all__'

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = temperature
        fields = '__all__'

class TvocSerializer(serializers.ModelSerializer):
    class Meta:
        model = tvoc
        fields = '__all__'

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = time
        fields = '__all__'

