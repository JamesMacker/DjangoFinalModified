from django.contrib import admin
from django.urls import path, include
from humidifierDjango import views
from .views import AllDataList

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/alldata/', AllDataList.as_view(), name='all-data'),
    path('', index_view, name='index'),
    path('fetch-data/', fetch_data_view, name='fetch-data'),
]