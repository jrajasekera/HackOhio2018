from django.contrib import admin
from .models import Source, SortBy, Category, Language, Country, SearchHistory
#Register models here

admin.site.register(Source)

admin.site.register(SortBy)

admin.site.register(Category)

admin.site.register(Language)

admin.site.register(Country)

admin.site.register(SearchHistory)
