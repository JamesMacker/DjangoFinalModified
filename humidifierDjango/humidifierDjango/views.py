from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import humidity, temperature, tvoc, time  # Assuming correct model names
from django.utils import timezone


def fetch_data_view(request):
    humidity_data = list(humidity.objects.all().values())
    temperature_data = list(temperature.objects.all().values())
    tvoc_data = list(tvoc.objects.all().values())
    time_data = list(time.objects.all().values())
    
    combined_data = {
        'humidity': humidity_data,
        'temperature': temperature_data,
        'air_quality': tvoc_data,
        'time': time_data,
    }
    
    return JsonResponse(combined_data, safe=False)

def index_view(request):
    # Your code to render the index page
    return render(request, 'index.html')

@csrf_exempt
def update_humidity(request):
    if request.method == 'POST':
        humidity_value = request.POST.get('humidity')
        # Assuming humidity_value is converted appropriately
        humidity_obj = humidity.objects.create(humidity_num=humidity_value)
        
        # Create or update a time model instance
        # This example creates a new time instance for every humidity update
        # Consider if you need to link these records or just log the update timestamp
        time_obj = time.objects.create(time_update=timezone.now())
        
        return JsonResponse({'status': 'success', 'humidity': humidity_value})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are accepted'}, status=400)
    
@csrf_exempt
def update_temperature(request):
    if request.method == 'POST':
        temperature_value = request.POST.get('temperature')
        # Assuming humidity_value is converted appropriately
        temperature_obj = temperature.objects.create(temperature_num=temperature_value)
        
        # Create or update a time model instance
        # This example creates a new time instance for every humidity update
        # Consider if you need to link these records or just log the update timestamp
        # time_obj = time.objects.create(time_update=timezone.now())
        
        return JsonResponse({'status': 'success', 'temperature': temperature_value})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are accepted'}, status=400)
    
@csrf_exempt
def update_tvoc(request):
    if request.method == 'POST':
        tvoc_value = request.POST.get('tvoc')
        # Assuming humidity_value is converted appropriately
        tvoc_obj = tvoc.objects.create(tvoc_num=tvoc_value)
        
        # Create or update a time model instance
        # This example creates a new time instance for every humidity update
        # Consider if you need to link these records or just log the update timestamp
        # time_obj = time.objects.create(time_update=timezone.now())
        
        return JsonResponse({'status': 'success', 'tvoc': tvoc_value})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are accepted'}, status=400)
