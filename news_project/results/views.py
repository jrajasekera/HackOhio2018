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
    return displayName

def getPartisanBiasDesc(bias):
    if -42 <= bias and bias <= -31:
        biasDesc = 'Most Extreme Left'
    elif -30 <= bias and bias <= -19:
        biasDesc = 'Hyper-Partisan Left'
    elif -18 <= bias and bias <= -7:
        biasDesc = 'Skews Left'
    elif -6 <= bias and bias <= 6:
        biasDesc = 'Neutral'
    elif 7 <= bias and bias <= 18:
        biasDesc = 'Skews Right'
    elif 19 <= bias and bias <= 30:
        biasDesc = 'Hyper-Partisan Right'
    elif 31 <= bias and bias <= 42:
        biasDesc = 'Most Extreme Right'
    else:
        biasDesc = 'Not Available'
    return biasDesc

def getFactualAccuracyDesc(accuracy):
    if 0 <= accuracy and accuracy <= 7:
        accuracyDesc = 'Contains Inaccurate/Fabricated Info'
    elif 8 <= accuracy and accuracy <= 15:
        accuracyDesc = 'Propaganda/Contains Misleading Info'
    elif 16 <= accuracy and accuracy <= 23:
        accuracyDesc = 'Selective or Incomplete Story; Unfair Persuasion'
    elif 24 <= accuracy and accuracy <= 31:
        accuracyDesc = 'Opinion; Fair Persuasion'
    elif 32 <= accuracy and accuracy <= 39:
        accuracyDesc = 'Analysis'
    elif 40 <= accuracy and accuracy <= 47:
        accuracyDesc = 'Complex Analysis OR Mix of Fact Reporting and Analysis'
    elif 48 <= accuracy and accuracy <= 55:
        accuracyDesc = 'Fact Reporting'
    elif 56 <= accuracy and accuracy <= 64:
        accuracyDesc = 'Original Fact Reporting'
    else:
        accuracyDesc = 'Not Available'
    return accuracyDesc

class Article:
    def __init__(self, site, title, date, url, author, articleText, partisanBias, factualAccuracy):
        self.site = getSourceDisplayName(site)
        self.title = title
        self.date = date
        self.url = url
        self.author = author
        self.articleText = cleanHtml(articleText)[:430]
        self.partisanBias = getPartisanBiasDesc(partisanBias)      
        self.factualAccuracy = getFactualAccuracyDesc(factualAccuracy)

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
    
