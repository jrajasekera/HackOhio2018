# results/urls.py
from django.urls import path

from .views import resultPage

urlpatterns = [
    path('', resultPage, name='results'),
]
