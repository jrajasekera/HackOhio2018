# pages/urls.py
from django.urls import path

from .views import resultsPage

urlpatterns = [
    path('resultsPage', resultsPage, name='results')
]
