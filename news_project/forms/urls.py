# pages/urls.py
from django.urls import path

from .views import searchPage

urlpatterns = [
    path('', searchPage, name='search')
]
