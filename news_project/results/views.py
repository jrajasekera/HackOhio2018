from django.shortcuts import render

#from django import forms
#from forms.forms as forms
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from forms.models import SearchHistory

def createRequest(keyword, sortBy, category, language):
    key = 'd46c2a4c9f2842c5bcf9b1948f61afbe'

    url = ('https://newsapi.org/v2/everything?'
              'q=' + keyword.replace(' ','+') + '&'
              'sortBy=' + sortBy + '&'
              'language=en&' 
              'apiKey=' + key)

    #response = requests.get(url)
    return url


@ensure_csrf_cookie
def resultPage(request):
    #return HttpResponse('Hello, World!')
    #return redirect("")

    latest = SearchHistory.objects.latest('id')
    # print(latest.keyword)
    # print(latest.sortBy)
    # print(latest.category)
    # print(latest.language)
    print(createRequest(latest.keyword, latest.sortBy, latest.category, latest.language))

    return render(request, 'results.html', {})
