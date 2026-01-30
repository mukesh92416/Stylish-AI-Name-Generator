from django.urls import path
from .views import stylish_name

urlpatterns = [
    path('stylish-name-generator/', stylish_name, name='stylish_name'),
]
