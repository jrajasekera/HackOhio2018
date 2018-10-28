from django.shortcuts import render
#from django import forms
#from forms.forms as forms
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from forms.models import SearchHistory




@ensure_csrf_cookie
def resultPage(request):
    #return HttpResponse('Hello, World!')
    #return redirect("")

    latest = SearchHistory.objects.latest('id')
    print(latest.keyword)
    print(latest.sortBy)
    print(latest.category)
    print(latest.language)
    return render(request, 'results.html', {})
