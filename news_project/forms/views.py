from django.http import Http404, request, HttpResponseRedirect
from django.urls import reverse
from django import forms
from .forms import SearchForm
from django.shortcuts import render_to_response, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Source, SortBy, Category, Language, Country, SearchHistory

def printFormItem(item,form):
    print((item + ' = ' + form.cleaned_data[item]))

def printForm(items, form):
    length = len(items)
    for x in range (0, length):
        printFormItem(items[x],form)
    return

def saveSearch(form):
    item = SearchHistory()
    item.category = form.cleaned_data['ddCategory']
    item.keyword = form.cleaned_data['inputKeywords']
    item.language = form.cleaned_data['ddLanguage']
    item.sortBy = form.cleaned_data['ddSortBy']
    item.save()
    return 

@ensure_csrf_cookie
def searchPage(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print('VALID FORM. NAVIGATING TO RESULTS PAGE')
            #  form.cleaned_data['my_form_field_name']
            formList = ["inputKeywords","ddSortBy", "ddCategory", "ddLanguage"]
            printForm(formList, form)
            #resultsURL = reverse('results', kwargs={'sortBy': 'date'})
            #return HttpResponseRedirect(resultsURL)
            saveSearch(form)
            return HttpResponseRedirect('http://127.0.0.1:8000/results/')
        else:
            print('FORM NOT VALID, RETURNING TO SEARCH PAGE')
    else:
        print('CREATING BLANK FORM')
        form = SearchForm()        
    #return render_to_response('search.html', {'form': form,})
    return render(request, 'search.html', {'form': form,})

