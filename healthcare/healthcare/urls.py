from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.urls import path, include

def home(request):
    return HttpResponse("Welcome to Healthcare API")

urlpatterns = [
    path('', home),  # <-- ye add karo
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/doctors/', include('doctors.urls')),
]