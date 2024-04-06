"""humidifierDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from humidifierDjango.views import index_view, fetch_data_view  # Corrected import
from .views import update_humidity

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index_view, name='index'),
    path('fetch-data/', fetch_data_view, name='fetch-data'),  # Correct usage of fetch_data_view
    path('update_humidity/', update_humidity, name='update_humidity'),
]

