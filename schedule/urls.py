from django.urls import path
from . import views

urlpatterns = [
    path('', views.sched, name='create_schedule'),  # This handles the root URL
    path('show', views.show, name='show_schedules'),  # Add a URL pattern for "View All Schedules"
    path('edit/<int:id>/', views.edit, name='edit_schedule'),
    path('update/<int:id>/', views.update, name='update_schedule'),
    path('delete/<int:id>/', views.destroy, name='delete_schedule'),
]
