from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', include('schedule.urls')),
    path('', include('schedule.urls')),  # Add this line to handle the root URL
]

 

