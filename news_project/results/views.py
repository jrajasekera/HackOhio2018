from django.shortcuts import render
#from django import forms
#from forms.forms as forms
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from forms.models import SearchHistory
import requests

def createRequest(keywords, sortBy, category, language):
    api_key = "d46c2a4c9f2842c5bcf9b1948f61afbe"
    url = "https://newsapi.org/v2/"
    
    '''read apikey'''
    
    if urlSort is not None:
        url += urlSort + '?'
        '''Three options'''

    if keywords is not None:
        url += 'q='+ keywords.toString
    
    if sources is not None:
        url += '&sources='+ sources
        country = None
        category = None
        '''source is not compatible with country or category'''

    if country is not None:
        url += '&country='+ country
    
    if category is not None:
        url += '&category='+ category
    
    if language is not None:
        url += '&language='+ language

    if fromDate is not None:
        url += '&from='+ fromDate

    if toDate is not None:
        url += '&to='+ toDate

    if sort is not None:
        url += '&sortBy='+ sort
    
    url+='apiKey='+ api_key
    '''response = requests.get(url
    '''
    return url
'''
def createRequest(keyword, sortBy, category, language):
    key = 'd46c2a4c9f2842c5bcf9b1948f61afbe'

    url = ('https://newsapi.org/v2/everything?'
              'q=' + keyword.replace(' ','+') + '&'
              'sortBy=' + sortBy + '&'
              'language=en&' 
              'apiKey=' + key)

    #response = requests.get(url)
    return url
'''


@ensure_csrf_cookie
def resultPage(request):
    #return HttpResponse('Hello, World!')
    #return redirect("")

    latest = SearchHistory.objects.latest('id')

    url = createRequest(latest.keyword, latest.sortBy, latest.category, latest.language)
    print('url = ' + url)
    
    return render(request, 'results.html', {})
