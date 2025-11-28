from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mesh_app.urls')),  # connect mesh_app endpoints
]
