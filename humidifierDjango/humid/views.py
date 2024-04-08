from django.shortcuts import render
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import humidity, temperature, tvoc, time
from .serializers import HumiditySerializer, TemperatureSerializer, TvocSerializer, TimeSerializer  # Assume these serializers are defined similarly to the previous example
# Create your views here.


class AllDataList(APIView):
    def get(self, request, format=None):
        data = {
            'humidity': HumiditySerializer(humidity.objects.all(), many=True).data,
            'temperature': TemperatureSerializer(temperature.objects.all(), many=True).data,
            'airQuality': TvocSerializer(tvoc.objects.all(), many=True).data,
            'time': TimeSerializer(time.objects.all(), many=True).data,
        }
        return Response(data)
    
def index_view(request):
    return render(request, 'index.html')

def fetch_data_view(request):
    data = {"message": "This is the data fetched."}  # Example data
    return JsonResponse(data)
