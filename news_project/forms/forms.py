from django import forms

class SearchForm(forms.Form):
    inputKeywords = forms.CharField(label='Topic', max_length=30)
