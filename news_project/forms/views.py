from django.http import Http404
from django.shortcuts import render

from .models import Source

def searchPage(request):
    sourceList = Source.objects
    context = {'sourceList': sourceList}
    return render(request, 'search.html', context)

