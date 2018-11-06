from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from forms.models import SearchHistory, Language, SortBy, Source
import requests
import json
import re

def createRequest(keywords, sort, language):
    apiKey = '06b22f60-789d-4906-9a37-1b7299747ecc'
    urlBase = 'https://webhose.io/filterWebContent?token=' + apiKey + '&format=json'

    defaultKeywords = 'world news'
    defaultSort = 'relevancy'
    defaultSize = '50'
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
        urlBase += '&sort=' + SortBy.objects.get(displaySortBy = sort).apiSortBy
    else:
        urlBase += '&sort=' + defaultSort

    # size
    urlBase += '&size=' + defaultSize

    # Extraction Accuracy Confidence
    urlBase += '&accuracy_confidence=' + defaultExtractionAccuracyConfidence

    # language
    if language is not None:
        urlBase += '&language=' + Language.objects.get(displayLang = language).apiLang
    else:
        urlBase += '&language=' + defaultLanguage

    # site_type
    urlBase += '&site_type=' + defaultSiteType

    # sites
    SiteList = Source.objects.all()
    for site in SiteList:
        urlBase += '&site=' + site.srcName

    return urlBase

def cleanHtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def getSourceRating(source):
    
    try:
        dbSrc = Source.objects.get(srcName = source)
        partisanBias = dbSrc.partisanBias
        factualAccuracy = dbSrc.factualAccuracy
    except Content.DoesNotExist:
        partisanBias = 1000
        factualAccuracy = 1000    
    
    return (partisanBias, factualAccuracy)

def getSourceDisplayName(source):
    try:
        dbSrc = Source.objects.get(srcName = source)
        displayName = dbSrc.displayName
    except Content.DoesNotExist:   
        displayName = source
class Article:
    def __init__(self, site, title, date, url, author, articleText, partisanBias, factualAccuracy):
        self.site = site
        self.title = title
        self.date = date
        self.url = url
        self.author = author
        self.articleText = cleanHtml(articleText)[:430]
        if partisanBias == 1000:
            self.partisanBias = 'Not Available'
        else:
            self.partisanBias = partisanBias

        if factualAccuracy == 1000:        
            self.factualAccuracy = 'Not Available'
        else:
            self.factualAccuracy = factualAccuracy

def JsonToArticles(json_data):
    posts = json_data['posts']
    results = len(posts)
    articleList = []

    for i in range(results):
        post = posts[i]
        site = post['thread']['site']
        title = post['title']
        date = post['published']
        url = post['url']
        author = post['author']
        articleText = post['text']
        partisanBias, factualAccuracy = getSourceRating(site)
        article = Article(site, title, date, url, author, articleText, partisanBias, factualAccuracy)

        if title != '':
            articleList.append(article)
    
    return articleList

@ensure_csrf_cookie
def resultPage(request):

    latest = SearchHistory.objects.latest('id')

    # create url query for api
    url = createRequest(latest.keyword, latest.sortBy, latest.language)
    print('url = ' + url)

    #send request
    try:
        JsonResponse = requests.get(url)
        jsonData = JsonResponse.json()
        articleList = JsonToArticles(jsonData)
        
        return render(request, 'results.html', {'articleList':articleList,})
        # return render(request, 'results.html', {})
    except requests.exceptions.RequestException as e:
        print('ERROR GETTING DATA FROM WEBHOSE API')
        print(e)     
        return render(request, 'results.html', {})
    
