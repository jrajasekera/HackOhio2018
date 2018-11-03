from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from forms.models import SearchHistory
import requests

def createRequest(keywords, sort, language, sites):
    apiKey = '06b22f60-789d-4906-9a37-1b7299747ecc'
    urlBase = 'https://webhose.io/filterWebContent?token=' + apiKey + '&format=json'

    defaultKeywords = 'world news'
    defaultSort = 'relevancy'
    defaultSize = '20'
    defaultExtractionAccuracyConfidence = 'high'
    defaultLanguage = 'english'
    defaultSiteType = 'news'

    # query/keyword
    if keywords is not None:
        urlBase += '&q=' + keywords.replace(' ','+')
    else:
        urlBase += '&q=' + defaultKeywords.replace(' ','+')

    # sort
    if sort is not None:
        urlBase += '&sort=' + sort
    else:
        urlBase += '&sort=' + defaultSort

    # size
    urlBase += '&size=' + defaultSize

    # Extraction Accuracy Confidence
    urlBase += '&accuracy_confidence=' + defaultExtractionAccuracyConfidence

    # language
    if language is not None:
        urlBase += '&language=' + language
    else:
        urlBase += '&language=' + defaultLanguage

    # site_type
    urlBase += '&site_type=' + defaultSiteType

    # sites
    for site in sites:
        if site is not None:
            urlBase += '&site=' + site

    return urlBase


@ensure_csrf_cookie
def resultPage(request):

    latest = SearchHistory.objects.latest('id')

    sites = ['cnn.com','foxnews.com','nytimes.com','washingtonpost.com'] 
    url = createRequest(latest.keyword, latest.sortBy, latest.language, sites)
    print('url = ' + url)

    return render(request, 'results.html', {})
