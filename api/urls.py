from django.urls import path
from .views import SeededVM

urlpatterns = [
    path('seededVM/', SeededVM.as_view(), name='SeededVM'),
]