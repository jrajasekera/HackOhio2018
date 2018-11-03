from django import forms
from crispy_forms.helper import FormHelper
from .models import Source, SortBy, Category, Language, Country


def QuerySetToList(qSet, keyName):
    newList = []
    lenth = len(list(qSet))
    for x in range (0,lenth):
        newList.append(list(qSet)[x][keyName])
    return newList

def listToTupleList(list):
    tupleList = []
    length = len(list)
    for x in range (0, length):
        tuple = (list[x],list[x])
        tupleList.append(tuple)
    return tupleList

def QuerySetToTupleList(qSet, keyName):
    listItems = QuerySetToList(qSet, keyName)
    return listToTupleList(listItems)

class SearchForm(forms.Form):
    inputKeywords = forms.CharField(label='Topic', max_length=30)

    #sortBy form
    sortKey = 'displaySortBy'
    sortQs = SortBy.objects.values(sortKey)
    ddSortBy = forms.CharField(widget=forms.Select(choices=QuerySetToTupleList(sortQs, sortKey)), initial = 'Relevance')
    

    # Language
    languageKey = 'displayLang'
    sortQs = Language.objects.values(languageKey)
    ddLanguage = forms.CharField(widget=forms.Select(choices=QuerySetToTupleList(sortQs, languageKey)), initial = 'English')

    #Source USE EVERY SOURCE FOR NOW

    # Country form USE US FOR NOW
    # countryKey = 'displayctry'
    # sortQs = Country.objects.values(countryKey)
    # countrySelect = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=QuerySetToTupleList(sortQs, countryKey))

    